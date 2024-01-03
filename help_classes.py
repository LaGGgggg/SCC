from math import hypot

from numpy import array, dot

from app_dataclasses import AdditionalLine, Color, Thickness
from help_functions import rotation_matrix


class Point:

    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point((self.x * scalar, self.y * scalar))

    def __truediv__(self, scalar):
        scalar = scalar or 1

        return Point((self.x / scalar, self.y / scalar))

    def __len__(self):
        return int(hypot(self.x, self.y))

    def get(self):
        return [self.x, self.y]


class Figure:

    def __init__(
            self,
            vertices: tuple[tuple[int | float, int | float, int | float], ...],
            vertices_names: tuple[str, ...],
            faces: tuple[tuple[int, ...], ...],
            additional_lines: tuple[AdditionalLine, ...] = None,
            faces_vertices_special_colors: tuple[tuple[int, tuple[tuple[int, int, Color, Thickness], ...]], ...] = None,
    ) -> None:
        """
        a 3D object that can rotate around the three axes
        :param vertices: a tuple of points (each has three coordinates)
        """
        self.__vertices = array(vertices)
        self.__vertices_names = vertices_names
        self.__rotation = [-45, 0.6, 0]  # radians around each axis
        self.__faces = faces
        self.__additional_lines = additional_lines or tuple()
        self.__faces_vertices_special_colors = faces_vertices_special_colors or tuple()

    def rotate(self, axis: int, o: int) -> None:
        self.__rotation[axis] += o

    @property
    def rotation(self) -> list[int, int, int]:
        return self.__rotation

    @property
    def vertices(self) -> array:
        return self.__vertices

    @vertices.setter
    def vertices(self, value):
        self.__vertices = value

    @property
    def vertices_names(self) -> tuple[str, ...]:
        return self.__vertices_names

    @property
    def faces(self) -> tuple[tuple[int, ...], ...]:
        return self.__faces

    @property
    def location(self) -> dot:
        return self.vertices.dot(rotation_matrix(*self.rotation).matrix)

    def get_face_vertices(self, face: tuple[int, ...]) -> list[tuple[int | float, int | float, int | float], ...]:

        location = self.location

        return [location[v] for v in face]

    def get_vertices_with_location(self) -> list[tuple[int | float, int | float, int | float], ...]:

        location = self.location

        return [location[v] for v in range(len(self.vertices))]

    @property
    def additional_lines(self) -> tuple[AdditionalLine, ...]:
        return self.__additional_lines

    @property
    def faces_vertices_special_colors(self) -> tuple[tuple[int, tuple[tuple[int, int, Color]]]]:
        return self.__faces_vertices_special_colors
