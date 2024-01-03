from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
VIOLET = Color(148, 0, 211)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__PYRAMID_SIDE = 4
__PYRAMID_HEIGHT = 5


PRISM_4_1 = Figure(
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
        (__PYRAMID_SIDE / 4, __PYRAMID_SIDE * 0.75, __PYRAMID_HEIGHT / 2),
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
        AdditionalLine(0, 6, (4,), color=BLUE, is_faces_inverted=True),
    ),
    faces_vertices_special_colors=(
        (2, ((4, 3, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (3, ((4, 3, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)

PRISM_4_2 = Figure(
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
        (__PYRAMID_SIDE * 1.2, __PYRAMID_SIDE * 1.2, 0),
        (__PYRAMID_SIDE * 1.2, __PYRAMID_SIDE * -0.2, 0),
        (__PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT * 1.2),
        (__PYRAMID_SIDE / 4, __PYRAMID_SIDE * 0.75, __PYRAMID_HEIGHT / 2),
    ),
    vertices_names=('C', 'D', 'B', 'A', 'S', 'O', 'x', 'y', 'z', 'M'),
    faces=(
        # counterclockwise:
        (0, 1, 3, 2),
        (4, 1, 0),
        (4, 3, 1),
        (4, 2, 3),
        (4, 0, 2),
    ),
    additional_lines=(
        AdditionalLine(0, 3, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(1, 2, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(3, 6, (0, 2, 3), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(1, 7, (0, 1, 2), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(4, 8, (1, 2, 3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(4, 5, (0,), thickness=THICKNESS_WIDE, is_always_hided=True),
        AdditionalLine(0, 9, (4,), color=BLUE, is_faces_inverted=True),
    ),
    faces_vertices_special_colors=(
        (2, ((4, 3, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (3, ((4, 3, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)
