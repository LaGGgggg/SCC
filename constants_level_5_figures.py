from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__PRISM_4_HEIGHT = 4
__PRISM_4_SIDE = 4

PRISM_4_1 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (__PRISM_4_SIDE, 0, 0),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, 0),
        (0, __PRISM_4_SIDE, 0),
        # top:
        (0, 0, __PRISM_4_HEIGHT),
        (__PRISM_4_SIDE, 0, __PRISM_4_HEIGHT),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT),
        # additional vertices:
        (0, __PRISM_4_SIDE * 0.4, __PRISM_4_HEIGHT),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 0.6),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 0.4),
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A1↓', 'B↓1', 'N', 'K', 'M'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(8, 9, (3,), color=BLUE),
        AdditionalLine(9, 10, (4,), color=BLUE),
        AdditionalLine(10, 5, (2,), color=BLUE),
        AdditionalLine(8, 5, (0,), color=BLUE),
    ),
)

PRISM_4_2 = Figure(
    vertices=(
        # bottom:
        (0, 0, 0),
        (__PRISM_4_SIDE, 0, 0),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, 0),
        (0, __PRISM_4_SIDE, 0),
        # top:
        (0, 0, __PRISM_4_HEIGHT),
        (__PRISM_4_SIDE, 0, __PRISM_4_HEIGHT),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT),
        # additional vertices:
        (__PRISM_4_SIDE * 1.2, __PRISM_4_SIDE, 0),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 1.2),
        (0, __PRISM_4_SIDE * -0.2, 0),
        (0, __PRISM_4_SIDE * 0.4, __PRISM_4_HEIGHT),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 0.6),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 0.4),
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A1↓', 'B↓1', 'x', 'z', 'y', 'N', 'K', 'M'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(2, 8, (1, 2, 4), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(7, 9, (0, 3, 4), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(0, 10, (1, 3, 5), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(11, 12, (3,), color=BLUE),
        AdditionalLine(12, 13, (4,), color=BLUE),
        AdditionalLine(13, 5, (2,), color=BLUE),
        AdditionalLine(11, 5, (0,), color=BLUE),
    ),
    faces_vertices_special_colors=(
        (2, ((3, 7, BLACK, Thickness(THICKNESS_WIDE)), (3, 0, BLACK, Thickness(THICKNESS_WIDE)))),
        (5, ((3, 7, BLACK, Thickness(THICKNESS_WIDE)), (2, 3, BLACK, Thickness(THICKNESS_WIDE)))),
        (0, ((3, 0, BLACK, Thickness(THICKNESS_WIDE)), (2, 3, BLACK, Thickness(THICKNESS_WIDE)))),
    ),
)
