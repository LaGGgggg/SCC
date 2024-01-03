from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)
THICKNESS_WIDE = 5
__PRISM_4_HEIGHT = 3
__PRISM_4_SIDE = 4


PRISM_1 = Figure(
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
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A↓1', 'B↓1'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(0, 2, (1,), color=BLUE),
        AdditionalLine(3, 4, (3,), color=BLUE),
    ),
)

PRISM_2 = Figure(
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
        # additional lines:
        (__PRISM_4_SIDE * 1.2, __PRISM_4_SIDE, 0),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 1.2),
        (0, __PRISM_4_SIDE * -0.2, 0),
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A↓1', 'B↓1', 'x', 'z', 'y'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(0, 2, (1,), color=BLUE),
        AdditionalLine(3, 4, (3,), color=BLUE),
        AdditionalLine(2, 8, (1, 2, 4), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(7, 9, (0, 3, 4), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(0, 10, (1, 3, 5), is_with_arrow=True, thickness=THICKNESS_WIDE),
    ),
    faces_vertices_special_colors=(
        (2, ((3, 7, BLACK, Thickness(THICKNESS_WIDE)), (3, 0, BLACK, Thickness(THICKNESS_WIDE)))),
        (5, ((3, 7, BLACK, Thickness(THICKNESS_WIDE)), (2, 3, BLACK, Thickness(THICKNESS_WIDE)))),
        (0, ((3, 0, BLACK, Thickness(THICKNESS_WIDE)), (2, 3, BLACK, Thickness(THICKNESS_WIDE)))),
    ),
)
