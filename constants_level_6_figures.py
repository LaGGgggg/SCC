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
        (3**0.5 / 2 * __PYRAMID_SIDE, __PYRAMID_SIDE / 2, 0),
        (0, __PYRAMID_SIDE, 0),
        # top:
        (3**0.5 / 6 * __PYRAMID_SIDE, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT),
        # additional vertices:
        (0, __PYRAMID_SIDE / 2, 0),
        (3**0.5 / 2 * __PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2 / 2, 0),
    ),
    vertices_names=('B', 'C', 'A', 'S', 'K', 'L'),
    faces=(
        # counterclockwise:
        (0, 1, 3),
        (1, 2, 3),
        (0, 3, 2),
        (2, 1, 0),
        # clockwise:
        # (0, 3, 1),
        # (1, 3, 2),
        # (2, 3, 0),
        # (0, 1, 2),
    ),
    additional_lines=(
        AdditionalLine(4, 5, (3,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(5, 3, (0,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(4, 3, (2,), is_faces_inverted=True, color=BLUE),
    ),
    faces_vertices_special_colors=(
        (0, ((0, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
        (2, (
            (0, 2, VIOLET, Thickness(THICKNESS_DEFAULT)),
            (2, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),
            (0, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),
        )),
        (1, ((2, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
        (3, ((0, 2, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
    ),
)

PYRAMID_2 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (3**0.5 / 2 * __PYRAMID_SIDE, __PYRAMID_SIDE / 2, 0),
        (0, __PYRAMID_SIDE, 0),
        # top:
        (3**0.5 / 6 * __PYRAMID_SIDE, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT),
        # additional vertices:
        (3**0.5 / 6 * __PYRAMID_SIDE, __PYRAMID_SIDE / 2, 0),
        (0, __PYRAMID_SIDE / 2, 0),
        (3**0.5 / 2 * __PYRAMID_SIDE / 2, __PYRAMID_SIDE / 2 / 2, 0),
        (0, __PYRAMID_SIDE * 1.2, 0),
        (0, __PYRAMID_SIDE / 2, __PYRAMID_HEIGHT * 1.2),
        (3**0.5 / 2 * __PYRAMID_SIDE * 1.2, __PYRAMID_SIDE / 2, 0),
    ),
    vertices_names=('B', 'C', 'A', 'S', 'O', 'K', 'L', 'x', 'z', 'y'),
    faces=(
        # counterclockwise:
        (0, 1, 3),
        (1, 2, 3),
        (0, 3, 2),
        (2, 1, 0),
        # clockwise:
        # (0, 3, 1),
        # (1, 3, 2),
        # (2, 3, 0),
        # (0, 1, 2),
    ),
    additional_lines=(
        AdditionalLine(2, 7, (0, 2, 3), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(5, 8, (2,), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(1, 9, (0,), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(1, 4, (3,), is_faces_inverted=True),
        AdditionalLine(4, 5, (3,), is_faces_inverted=True),
        AdditionalLine(3, 4, (0,), is_always_hided=True),
        AdditionalLine(5, 6, (3,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(6, 3, (0,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(5, 3, (2,), is_faces_inverted=True, color=BLUE),
    ),
    faces_vertices_special_colors=(
        (0, ((0, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
        (2, (
            (0, 2, VIOLET, Thickness(THICKNESS_DEFAULT)),
            (2, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),
            (0, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),
        )),
        (1, ((2, 3, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
        (3, ((0, 2, VIOLET, Thickness(THICKNESS_DEFAULT)),)),
    ),
)
