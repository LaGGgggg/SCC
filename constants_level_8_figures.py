from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
VIOLET = Color(148, 0, 211)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__PYRAMID_HEIGHT = 4
__PYRAMID_SIDE = 4

PYRAMID_1 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (__PYRAMID_SIDE, 0, 0),
        (0, __PYRAMID_SIDE, 0),
        (__PYRAMID_SIDE, __PYRAMID_SIDE, 0),
        # top:
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT),
        # additional vertices:
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, 0),
        (3, 1, 2),  # calculated for __PYRAMID_HEIGHT = __PYRAMID_SIDE = 4
    ),
    vertices_names=('C', 'D', 'B', 'A', 'S', 'O', 'M'),
    faces=(
        # counterclockwise:
        (0, 1, 3, 2),
        (4, 1, 0),
        (4, 3, 1),
        (4, 2, 3),
        (4, 0, 2),
    ),
    additional_lines=(
        AdditionalLine(2, 6, (0,), is_always_hided=True),
        AdditionalLine(3, 6, (2,), is_faces_inverted=True, color=BLUE),
    ),
)

PYRAMID_2 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (__PYRAMID_SIDE, 0, 0),
        (0, __PYRAMID_SIDE, 0),
        (__PYRAMID_SIDE, __PYRAMID_SIDE, 0),
        # top:
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT),
        # additional vertices:
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, 0),
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT * 1.2),
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE * 1.2, 0),
        (__PYRAMID_SIDE * 1.2, __PYRAMID_SIDE / 2, 0),
        (3, 1, 2),  # calculated for __PYRAMID_HEIGHT = __PYRAMID_SIDE = 4
        # silent:
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE, 0),
        (__PYRAMID_SIDE, __PYRAMID_SIDE / 2, 0),
    ),
    vertices_names=('C', 'D', 'B', 'A', 'S', 'O', 'z', 'x', 'y', 'M'),
    faces=(
        # counterclockwise:
        (0, 1, 3, 2),
        (4, 1, 0),
        (4, 3, 1),
        (4, 2, 3),
        (4, 0, 2),
    ),
    additional_lines=(
        AdditionalLine(5, 4, (0,), thickness=THICKNESS_WIDE, is_always_hided=True),
        AdditionalLine(4, 6, (1, 2, 3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(10, 5, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(10, 7, (1,), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(11, 5, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(11, 8, (2,), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(0, 3, (0,), is_faces_inverted=True),
        AdditionalLine(1, 2, (0,), is_faces_inverted=True),
        AdditionalLine(2, 9, (0,), is_always_hided=True),
        AdditionalLine(3, 9, (2,), is_faces_inverted=True, color=BLUE),
    ),
)
