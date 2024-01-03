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
        # additional vertices:
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, -2),
        (__PYRAMID_SIDE * 3 ** 0.5 * -0.1, __PYRAMID_SIDE * -0.1, -2),
        (__PYRAMID_SIDE * 3**0.5 * 0.75, __PYRAMID_SIDE * -0.25, -2),
        (__PYRAMID_SIDE * 3**0.5 / 4.25, __PYRAMID_SIDE * 3**0.5 / 1.4, -2),
        (0.71, 4.6375, -2),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, (__PYRAMID_HEIGHT - 2) * 1.2),
        (1.25, 0.73, -0.05),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (3.83, 0.77, 0.1),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (2.58, 0.08, 0.13),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
    ),
    vertices_names=('A', 'B', 'C', 'D', 'E', 'F', 'S', 'O', '', '', '', '', '', 'N', 'M', 'K'),
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
        AdditionalLine(7, 6, (0,), is_always_hided=True),
        AdditionalLine(3, 14, (3,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(14, 15, (2,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(15, 13, (1,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(13, 5, (6,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(0, 0, (0,), is_always_visible=True, color=BLUE, thickness=THICKNESS_WIDE),
        AdditionalLine(3, 5, (0,), is_faces_inverted=True, color=BLUE),
    ),
)

PYRAMID_2 = Figure(
    vertices=(
        (0, 0, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * -0.5, -2),
        (__PYRAMID_SIDE * 3**0.5, 0, -2),
        (__PYRAMID_SIDE * 3**0.5, __PYRAMID_SIDE, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 1.5, -2),
        (0, __PYRAMID_SIDE, -2),
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, __PYRAMID_HEIGHT - 2),
        # additional vertices:
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, -2),
        (__PYRAMID_SIDE * 3 ** 0.5 * -0.1, __PYRAMID_SIDE * -0.1, -2),
        (__PYRAMID_SIDE * 3**0.5 * 0.75, __PYRAMID_SIDE * -0.25, -2),
        (__PYRAMID_SIDE * 3**0.5 / 4.25, __PYRAMID_SIDE * 3**0.5 / 1.4, -2),
        (0.71, 4.6375, -2),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (__PYRAMID_SIDE * (3**0.5 / 2), __PYRAMID_SIDE * 0.5, (__PYRAMID_HEIGHT - 2) * 1.2),
        (1.25, 0.73, -0.05),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (3.83, 0.77, 0.1),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
        (2.58, 0.08, 0.13),  # calculated for: __PYRAMID_SIDE = 3, __PYRAMID_HEIGHT = 4
    ),
    vertices_names=('A', 'B', 'C', 'D', 'E', 'F', 'S', 'O', 'x', '', '', 'y', 'z', 'N', 'M', 'K'),
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
        AdditionalLine(7, 7, (0,), thickness=THICKNESS_WIDE, is_always_visible=True),
        AdditionalLine(3, 0, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(0, 8, (3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(10, 9, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(10, 11, (5,), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(7, 6, (0,), is_always_hided=True),
        AdditionalLine(6, 12, (1, 2, 3, 4, 5), is_faces_inverted=True, is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(3, 14, (3,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(14, 15, (2,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(15, 13, (1,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(13, 5, (6,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(0, 0, (0,), is_always_visible=True, color=BLUE, thickness=THICKNESS_WIDE),
        AdditionalLine(3, 5, (0,), is_faces_inverted=True, color=BLUE),
    ),
)
