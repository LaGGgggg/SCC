from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5
BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)

__PYRAMID_SIDE = 3
__PYRAMID_HEIGHT = 4

PYRAMID_1 = Figure(
    vertices=(
        (0, 0, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * -0.5, -2),
        (__PYRAMID_SIDE * 3**0.5, 0, -2),
        (__PYRAMID_SIDE * 3**0.5, __PYRAMID_SIDE, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 1.5, -2),
        (0, __PYRAMID_SIDE, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, __PYRAMID_HEIGHT - 2),
        (3**0.5 * __PYRAMID_SIDE / 2, __PYRAMID_SIDE, __PYRAMID_HEIGHT / 2 - 2),
    ),
    vertices_names=('A', 'B', 'C', 'D', 'E', 'F', 'S', 'M'),
    faces=(
        (0, 1, 2, 3, 4, 5),  # clockwise
        (6, 1, 0),  # clockwise
        (6, 2, 1),  # clockwise
        (6, 3, 2),  # clockwise
        (6, 4, 3),  # clockwise
        (6, 5, 4),  # clockwise
        (0, 5, 6),  # clockwise
    ),
    additional_lines=(
        AdditionalLine(2, 7, (0,), is_always_hided=True, color=BLUE),
    ),
    faces_vertices_special_colors=(
        (0, ((0, 1, BLACK, Thickness(THICKNESS_WIDE)),)),
        (1, ((6, 1, BLUE, Thickness(THICKNESS_DEFAULT)), (0, 1, BLACK, Thickness(THICKNESS_WIDE)))),
        (2, ((6, 1, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)

PYRAMID_2 = Figure(
    vertices=(
        (0, 0, -2), (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * -0.5, -2), (__PYRAMID_SIDE * 3**0.5, 0, -2),
        (__PYRAMID_SIDE * 3**0.5, __PYRAMID_SIDE, -2), (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 1.5, -2),
        (0, __PYRAMID_SIDE, -2), (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, __PYRAMID_HEIGHT - 2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * -0.5, __PYRAMID_HEIGHT * 1.2 - 2),
        (__PYRAMID_SIDE * -0.32, __PYRAMID_SIDE * 0.2, -2), (__PYRAMID_SIDE * 3**0.5 * 1.2, __PYRAMID_SIDE * 1.6, -2),
        (3**0.5 * __PYRAMID_SIDE / 2, __PYRAMID_SIDE, __PYRAMID_HEIGHT / 2 - 2),
    ),
    vertices_names=('A', 'B', 'C', 'D', 'E', 'F', 'S', 'z', 'x', 'y', 'M'),
    faces=(
        (0, 1, 2, 3, 4, 5),  # clockwise
        (6, 1, 0),  # clockwise
        (6, 2, 1),  # clockwise
        (6, 3, 2),  # clockwise
        (6, 4, 3),  # clockwise
        (6, 5, 4),  # clockwise
        (0, 5, 6),  # clockwise
    ),
    additional_lines=(
        AdditionalLine(1, 7, (4, 5), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(0, 8, (3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(3, 9, (5, 6), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(1, 3, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(2, 10, (0,), is_always_hided=True, color=BLUE),
    ),
    faces_vertices_special_colors=(
        (0, ((0, 1, BLACK, Thickness(THICKNESS_WIDE)),)),
        (1, ((6, 1, BLUE, Thickness(THICKNESS_DEFAULT)), (0, 1, BLACK, Thickness(THICKNESS_WIDE)))),
        (2, ((6, 1, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)
