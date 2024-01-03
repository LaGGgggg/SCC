from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
VIOLET = Color(148, 0, 211)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__PRISM_HEIGHT = 4
__PRISM_SIDE = 3

PRISM_3_1 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (3**0.5 / 2 * __PRISM_SIDE, __PRISM_SIDE / 2, 0),
        (0, __PRISM_SIDE, 0),
        # top:
        (0, 0, __PRISM_HEIGHT),
        (3 ** 0.5 / 2 * __PRISM_SIDE, __PRISM_SIDE / 2, __PRISM_HEIGHT),
        (0, __PRISM_SIDE, __PRISM_HEIGHT),
        # additional vertices:
        (0, __PRISM_SIDE / 2, 0),
        (0, __PRISM_SIDE / 2, __PRISM_HEIGHT),
    ),
    vertices_names=('A', 'B', 'C', 'A1', 'B1', 'C1', 'O', ''),
    faces=(
        # counterclockwise:
        (0, 1, 2),
        (5, 4, 3),
        (1, 0, 3, 4),
        (2, 1, 4, 5),
        (0, 2, 5, 3),
    ),
    additional_lines=(
        AdditionalLine(0, 4, (2,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(1, 5, (3,), is_faces_inverted=True, color=BLUE),
    ),
)

PRISM_3_2 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (3**0.5 / 2 * __PRISM_SIDE, __PRISM_SIDE / 2, 0),
        (0, __PRISM_SIDE, 0),
        # top:
        (0, 0, __PRISM_HEIGHT),
        (3 ** 0.5 / 2 * __PRISM_SIDE, __PRISM_SIDE / 2, __PRISM_HEIGHT),
        (0, __PRISM_SIDE, __PRISM_HEIGHT),
        # additional vertices:
        (0, __PRISM_SIDE / 2, 0),
        (0, __PRISM_SIDE / 2, __PRISM_HEIGHT),
        (0, __PRISM_SIDE / 2, __PRISM_HEIGHT * 1.2),
        (3 ** 0.5 / 2 * __PRISM_SIDE * 1.2, __PRISM_SIDE / 2, 0),
        (0, __PRISM_SIDE * 1.2, 0),
    ),
    vertices_names=('A', 'B', 'C', 'A1', 'B1', 'C1', 'O', '', 'z', 'y', 'x'),
    faces=(
        # counterclockwise:
        (0, 1, 2),
        (5, 4, 3),
        (1, 0, 3, 4),
        (2, 1, 4, 5),
        (0, 2, 5, 3),
    ),
    additional_lines=(
        AdditionalLine(6, 7, (4,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(7, 8, (4, 1), thickness=THICKNESS_WIDE, is_faces_inverted=True, is_with_arrow=True),
        AdditionalLine(6, 1, (0,), thickness=THICKNESS_WIDE, is_faces_inverted=True),
        AdditionalLine(1, 9, (0, 2, 3), thickness=THICKNESS_WIDE, is_faces_inverted=True, is_with_arrow=True),
        AdditionalLine(2, 10, (0, 3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True, is_faces_inverted=True),
        AdditionalLine(0, 4, (2,), is_faces_inverted=True, color=BLUE),
        AdditionalLine(1, 5, (3,), is_faces_inverted=True, color=BLUE),
    ),
)
