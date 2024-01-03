from typing import Iterable
from sys import exit

import pygame
from numpy import cross, linalg
from shapely.geometry import Polygon, LineString

from constants import X, Y, Z, BLACK, WHITE, BLUE, LEVELS, THICKNESS_DEFAULT, THICKNESS_WIDE
from help_classes import Point
from help_functions import get_current_level
from app_dataclasses import Color


class Main:

    def __init__(
            self,
            background_color: Color,
            main_color: Color,
            debug: bool = False,
            debug_colors: bool = False,
            debug_level_shift: int = 0,
    ) -> None:

        self.background_color = background_color
        self.main_color = main_color
        self.debug = debug
        self.debug_colors = debug_colors

        counter_clockwise = 0.05  # radians
        clockwise = -counter_clockwise

        self.__keys = {
            pygame.K_s: (X, clockwise),
            pygame.K_w: (X, counter_clockwise),
            pygame.K_a: (Y, clockwise),
            pygame.K_d: (Y, counter_clockwise),
            pygame.K_e: (Z, clockwise),
            pygame.K_q: (Z, counter_clockwise),
        }

        self.__keys_tap = {
            pygame.K_u: self.__move_to_next_level_stage_or_level,
        }

        initial_screen_size = (900, 900)

        pygame.init()

        self.__font = pygame.font.SysFont('Times New Roman', 24)
        self.__small_font = pygame.font.SysFont('Times New Roman', 10)

        pygame.display.set_caption('Control -   w, s : X    a, d : Y    q, e : Z')

        self.__clock = pygame.time.Clock()

        self.__screen = pygame.display.set_mode(initial_screen_size, pygame.RESIZABLE)

        self.__levels = get_current_level(LEVELS)

        for _ in range(debug_level_shift):
            next(self.__levels)

        self.__current_level = None
        self.__current_level_stage = None
        self.__level_stage_text = None

        self.__mainloop()

    def __fit(self, vec: Iterable[int]) -> list[int, int]:
        """
        ignore the z-element (creating a very cheap projection), and scale x, y to the coordinates of the screen
        """
        # notice that len(self.__size) is 2, hence zip(vec, self.__size) ignores the vector's last coordinate
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, self.__screen.get_size())]

    def __handle_events(self) -> None:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key in self.__keys_tap:
                    self.__keys_tap[event.key]()

            elif event.type == pygame.VIDEORESIZE:
                self.__screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_0]:
            print(8, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][0] += 0.01
            self.__shape.vertices = new_vertices

        elif keys_pressed[pygame.K_9]:
            print(9, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][0] -= 0.01
            self.__shape.vertices = new_vertices

        elif keys_pressed[pygame.K_7]:
            print(7, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][2] += 0.01
            self.__shape.vertices = new_vertices

        elif keys_pressed[pygame.K_8]:
            print(8, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][2] -= 0.01
            self.__shape.vertices = new_vertices

        elif keys_pressed[pygame.K_5]:
            print(5, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][1] += 0.01
            self.__shape.vertices = new_vertices

        elif keys_pressed[pygame.K_6]:
            print(6, self.__shape.vertices[-1])
            new_vertices = self.__shape.vertices
            new_vertices[-1][1] -= 0.01
            self.__shape.vertices = new_vertices

        for key in self.__keys:
            if keys_pressed[key]:
                self.__shape.rotate(*self.__keys[key])

    def __draw_dashed_line(
            self,
            start_vertice: tuple[int, int, int],
            end_vertice: tuple[int, int, int],
            line_color: tuple[int, int, int],
            thickness: int,
    ) -> None:

        origin = Point(self.__fit(start_vertice))
        target = Point(self.__fit(end_vertice))
        dash_length = 20
        displacement = target - origin
        length = len(displacement)
        slope = displacement / length

        for i in range(2, int(length / dash_length), 2):
            start = origin + slope * i * dash_length
            end = origin + slope * (i - 1) * dash_length

            pygame.draw.line(self.__screen, line_color, start.get(), end.get(), thickness)

        end_dot = origin + slope * (length / dash_length) * dash_length

        pygame.draw.circle(self.__screen, line_color, end_dot.get(), thickness - 1)

    @staticmethod
    def __is_face_visible(vertices) -> bool:

        n = cross(vertices[1] - vertices[0], vertices[2] - vertices[0])

        nn = n / linalg.norm(n)

        return False if nn[2] < 0 else True

    def __draw_line(
            self,
            is_dashed_line: bool,
            start_vertice: tuple[int, int, int],
            end_vertice: tuple[int, int, int],
            thickness: int,
            line_color: Color | None = None,
            dashed_line_color: Color | None = None,
    ) -> None:

        if is_dashed_line:

            color: Color = dashed_line_color or self.main_color if not self.debug_colors else BLUE

            self.__draw_dashed_line(start_vertice, end_vertice, color.get(), thickness)

        else:

            color: Color = line_color or self.main_color

            pygame.draw.line(
                self.__screen, color.get(), self.__fit(start_vertice), self.__fit(end_vertice), thickness
            )

            pygame.draw.circle(self.__screen, color.get(), self.__fit(end_vertice), thickness - 1)

    def __draw_only_word(
            self,
            word: str,
            font: pygame.font.Font,
            small_font: pygame.font.Font,
            color: Color,
            x: int,
            y: int,
            max_width: int,
            start_dest: list[int, int],
            is_next_line_big_gap: bool,
    ) -> tuple[int, int, int, int]:

        # first tuple integer indicates y offset
        word_surfaces: list[tuple[int, pygame.surface.Surface]]

        if '↓' in word:

            word_surfaces = []
            is_next_symbol_small = False

            for s in word:

                if s == '↓':

                    is_next_symbol_small = True

                    continue

                if is_next_symbol_small:

                    word_surfaces.append((15, small_font.render(s, False, color.get())))

                    is_next_symbol_small = False

                else:
                    word_surfaces.append((0, font.render(s, False, color.get())))

        else:
            word_surfaces = [(0, font.render(word, False, color.get()))]

        word_width = sum([surface_tuple[1].get_width() for surface_tuple in word_surfaces])
        word_height = sum([surface_tuple[1].get_height() for surface_tuple in word_surfaces])

        if x + word_width >= max_width:
            # go to a new line

            x = start_dest[0]
            y += word_height + (60 if is_next_line_big_gap else 20)

        word_surfaces_x = x

        for word_surface in word_surfaces:

            self.__screen.blit(word_surface[1], (word_surfaces_x, y + word_surface[0]))

            word_surfaces_x += word_surface[1].get_width()

        return word_width, word_height, x, y

    def __draw_text(
            self,
            font: pygame.font.Font,
            small_font: pygame.font.Font,
            text: str,
            color: Color,
            start_dest: list[int, int] = None,
    ) -> None:

        if start_dest is None:
            start_dest = [30, 30]

        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.

        space_width = font.size(' ')[0]

        max_width, max_height = self.__screen.get_size()

        x, y = start_dest

        for line in words:

            word_height = 0
            word_width = 0
            is_next_line_big_gap = False

            for i, word in enumerate(line):

                is_with_image = False
                is_big_image = False
                is_small_image = False

                if '{%render_image#' in word:
                    is_with_image = True

                elif '{%render_big_image#' in word:

                    is_with_image = True
                    is_big_image = True
                    is_next_line_big_gap = True

                elif '{%render_small_image#' in word:

                    is_with_image = True
                    is_small_image = True

                if is_with_image:

                    if is_big_image:

                        before_image_path, image_path_raw = word.split('{%render_big_image#')
                        y_shift = 20

                    elif is_small_image:

                        before_image_path, image_path_raw = word.split('{%render_small_image#')
                        y_shift = 0

                    else:

                        before_image_path, image_path_raw = word.split('{%render_image#')
                        y_shift = 10

                    if before_image_path:
                        _, _, x, y = self.__draw_only_word(
                            word, font, small_font, color, x, y, max_width, start_dest, is_next_line_big_gap
                        )

                    image_path, after_image_path = image_path_raw.split('%}')

                    word = after_image_path

                    image = pygame.image.load(image_path)

                    word_width, word_height = image.get_size()

                    if x + word_width >= max_width:
                        # go to a new line

                        x = start_dest[0]
                        y += word_height + (60 if is_next_line_big_gap else 20)

                    self.__screen.blit(image, (x, y - y_shift))

                    x += word_width
                    word_width = 0

                if word:
                    word_width, word_height, x, y = self.__draw_only_word(
                        word, font, small_font, color, x, y, max_width, start_dest, is_next_line_big_gap
                    )

                x += word_width + space_width

            # go to a new line:
            x = start_dest[0]
            y += word_height

    def __draw_arrow(
            self,
            start: pygame.Vector2,
            end: pygame.Vector2,
            color: Color,
            head_width: int = 10,
            head_height: int = 8,
    ) -> None:

        arrow = start - end
        angle = arrow.angle_to(pygame.Vector2(0, -1))

        # Create the triangle head around the origin
        head_verts = [
            pygame.Vector2(0, head_height / 2),  # Center
            pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
            pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
        ]

        # Rotate and translate the head into place
        translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)

        for i in range(len(head_verts)):

            head_verts[i].rotate_ip(-angle)
            head_verts[i] += translation
            head_verts[i] += start

        pygame.draw.polygon(self.__screen, color.get(), head_verts)

    def __draw_shape(
            self, thickness=THICKNESS_DEFAULT, dash_length: int = 20, additional_line_chunk_size: int = 4
    ) -> None:

        visible_polygons = []

        for face_index, face in enumerate(self.__shape.faces):

            face_vertices = self.__shape.get_face_vertices(face)

            last_vertice = first_vertice = None

            is_dashed_line = self.__is_face_visible(face_vertices)

            face_vertices_special_colors = tuple()

            for current_face_vertices_special_colors in self.__shape.faces_vertices_special_colors:
                if current_face_vertices_special_colors[0] == face_index:

                    face_vertices_special_colors = current_face_vertices_special_colors[1]

                    break

            last_face_vertice_index = 0

            for face_vertice_index, vertice in enumerate(face_vertices):

                if last_vertice is not None:

                    line_color = self.main_color
                    line_thickness = thickness

                    for face_vertices_special_colors_part in face_vertices_special_colors:
                        if (face[face_vertice_index - 1] in face_vertices_special_colors_part and
                                face[face_vertice_index] in face_vertices_special_colors_part):

                            line_color = face_vertices_special_colors_part[2]
                            line_thickness = face_vertices_special_colors_part[3].thickness

                            break

                    self.__draw_line(
                        is_dashed_line,
                        last_vertice,
                        vertice,
                        line_thickness,
                        line_color=line_color,
                        dashed_line_color=line_color,
                    )

                else:
                    first_vertice = vertice

                last_vertice = vertice

                last_face_vertice_index = face_vertice_index

            if not is_dashed_line:

                vertices_2d_coordinates = []

                for fvertice in face_vertices:

                    fitted_vertice = self.__fit(fvertice)

                    vertices_2d_coordinates.append(fitted_vertice)

                visible_polygons.append(Polygon(vertices_2d_coordinates))

            line_color = self.main_color
            line_thickness = thickness

            for face_vertices_special_colors_part in face_vertices_special_colors:
                if (face[last_face_vertice_index] in face_vertices_special_colors_part and
                        face[0] in face_vertices_special_colors_part):

                    line_color = face_vertices_special_colors_part[2]
                    line_thickness = face_vertices_special_colors_part[3].thickness

                    break

            self.__draw_line(
                is_dashed_line,
                last_vertice,
                first_vertice,
                line_thickness,
                line_color=line_color,
                dashed_line_color=line_color,
            )

        for additional_line in self.__shape.additional_lines:

            additional_line_vertices = self.__shape.get_face_vertices(
                (additional_line.start_vertice, additional_line.end_vertice)
            )

            faces_vertices = \
                [self.__shape.get_face_vertices(self.__shape.faces[face]) for face in additional_line.faces]

            if self.debug:
                print([self.__is_face_visible(self.__shape.get_face_vertices(face)) for face in self.__shape.faces])

            if additional_line.is_with_arrow:
                self.__draw_arrow(
                    pygame.Vector2(self.__fit(additional_line_vertices[0])),
                    pygame.Vector2(self.__fit(additional_line_vertices[1])),
                    additional_line.color or self.main_color,
                )

            is_draw_not_dashed_line = all([self.__is_face_visible(face_vertices) for face_vertices in faces_vertices])

            if additional_line.is_faces_inverted:
                is_draw_not_dashed_line = False if is_draw_not_dashed_line else True

            if additional_line.is_always_hided:
                self.__draw_line(
                    True,
                    additional_line_vertices[0],
                    additional_line_vertices[1],
                    additional_line.thickness,
                    line_color=additional_line.color or self.main_color,
                    dashed_line_color=additional_line.color or self.main_color,
                )

            elif additional_line.is_always_visible:
                self.__draw_line(
                    False,
                    additional_line_vertices[0],
                    additional_line_vertices[1],
                    additional_line.thickness,
                    line_color=additional_line.color or self.main_color,
                    dashed_line_color=additional_line.color or self.main_color,
                )

            elif is_draw_not_dashed_line:
                self.__draw_line(
                    False,
                    additional_line_vertices[0],
                    additional_line_vertices[1],
                    additional_line.thickness,
                    line_color=additional_line.color or self.main_color,
                    dashed_line_color=additional_line.color or self.main_color,
                )

            else:

                point_1_not_fitted = self.__fit(additional_line_vertices[0])
                point_2_not_fitted = self.__fit(additional_line_vertices[1])

                points_line = LineString([point_1_not_fitted, point_2_not_fitted])

                last_point = None

                line_length = int(
                    ((point_1_not_fitted[0] - point_2_not_fitted[0])**2 +
                     (point_1_not_fitted[1] - point_2_not_fitted[1])**2)**0.5
                )

                parts_to_empty_or_full = dash_length // additional_line_chunk_size
                is_full_part_now = True

                for i in range(0, line_length, additional_line_chunk_size):

                    current_point = points_line.interpolate(i)

                    if not last_point:

                        last_point = current_point

                        continue

                    is_dashed_line = False

                    for pol in visible_polygons:
                        if pol.contains(last_point) or pol.contains(current_point):

                            is_dashed_line = True

                            break

                    if is_dashed_line:

                        if parts_to_empty_or_full > 0:
                            parts_to_empty_or_full -= 1

                        elif parts_to_empty_or_full == 0:

                            parts_to_empty_or_full = dash_length // additional_line_chunk_size

                            is_full_part_now = False if is_full_part_now else True

                        if is_full_part_now:
                            pygame.draw.line(
                                self.__screen,
                                additional_line.color.get() if additional_line.color else self.main_color.get(),
                                (last_point.x, last_point.y),
                                (current_point.x, current_point.y),
                                additional_line.thickness,
                            )

                    else:
                        pygame.draw.line(
                            self.__screen,
                            additional_line.color.get() if additional_line.color else self.main_color.get(),
                            (last_point.x, last_point.y),
                            (current_point.x, current_point.y),
                            additional_line.thickness,
                        )

                    last_point = current_point

        for vertice, vertice_name in zip(self.__shape.get_vertices_with_location(), self.__shape.vertices_names):

            text_destination = [i + 10 for i in self.__fit(vertice)]

            self.__draw_text(self.__font, self.__small_font, vertice_name, self.main_color, text_destination)

    def __draw_text_handler(self) -> None:
        self.__draw_text(self.__font, self.__small_font, self.__level_stage_text, self.main_color)

    def __move_to_next_level_stage_text(self) -> None:
        self.__level_stage_text = self.__current_level.texts.texts[self.__current_level_stage]

    def __move_to_next_level_stage_shape(self) -> None:
        self.__shape = self.__current_level.figures.figures[self.__current_level_stage]

    def __move_to_next_level_stage_text_and_shape(self) -> None:

        self.__move_to_next_level_stage_text()
        self.__move_to_next_level_stage_shape()

    def __move_to_next_level(self) -> None:

        self.__current_level = next(self.__levels)

        if self.__current_level is None:
            exit()

        self.__current_level_stage = 0

        self.__move_to_next_level_stage_text_and_shape()

    def __move_to_next_level_stage(self) -> None:

        self.__current_level_stage += 1

        self.__move_to_next_level_stage_text_and_shape()

    def __move_to_next_level_stage_or_level(self) -> None:

        if self.__current_level_stage + 1 >= len(self.__current_level.texts.texts):
            self.__move_to_next_level()

        else:
            self.__move_to_next_level_stage()

    def __mainloop(self) -> None:

        self.__move_to_next_level()

        while True:

            self.__handle_events()

            self.__screen.fill(self.background_color.get())

            self.__draw_shape()
            self.__draw_text_handler()

            pygame.display.flip()
            self.__clock.tick(40)


if __name__ == '__main__':
    Main(WHITE, BLACK, debug=False, debug_colors=False, debug_level_shift=11)
