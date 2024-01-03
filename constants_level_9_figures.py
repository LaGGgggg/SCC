from app_dataclasses import AdditionalLine, Color
from help_classes import Figure


BLUE = Color(0, 0, 255)
VIOLET = Color(148, 0, 211)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__PRISM_4_SIDE = 4
__PRISM_4_HEIGHT = 5


PRISM_4_1 = Figure(
    vertices=(
        (0, 0, -1),
        (__PRISM_4_SIDE, 0, -1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, -1),
        (0, __PRISM_4_SIDE, -1),
        (0, 0, __PRISM_4_HEIGHT - 1),
        (__PRISM_4_SIDE, 0, __PRISM_4_HEIGHT - 1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT - 1),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT - 1),
        # additional vertices:
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT / 2 - 1),
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A↓1', 'B↓1', 'M'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(8, 8, (0,), is_always_visible=True, thickness=THICKNESS_WIDE, color=BLUE),
        AdditionalLine(6, 1, (2,), color=BLUE),
        AdditionalLine(1, 4, (5,), color=BLUE),
        AdditionalLine(4, 6, (0,), color=BLUE),
    ),
)

PRISM_4_2 = Figure(
    vertices=(
        (0, 0, -1),
        (__PRISM_4_SIDE, 0, -1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, -1),
        (0, __PRISM_4_SIDE, -1),
        (0, 0, __PRISM_4_HEIGHT - 1),
        (__PRISM_4_SIDE, 0, __PRISM_4_HEIGHT - 1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT - 1),
        (0, __PRISM_4_SIDE, __PRISM_4_HEIGHT - 1),
        # additional vertices:
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT * 1.2 - 1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE * -0.2, -1),
        (__PRISM_4_SIDE * -0.2, __PRISM_4_SIDE, -1),
        (__PRISM_4_SIDE, __PRISM_4_SIDE, __PRISM_4_HEIGHT / 2 - 1),
    ),
    vertices_names=('C', 'D', 'A', 'B', 'C↓1', 'D↓1', 'A↓1', 'B↓1', 'z', 'x', 'y', 'M'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(6, 8, (0, 2, 4), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(1, 9, (1, 2, 5), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(3, 10, (1, 3, 4), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(11, 11, (0,), is_always_visible=True, thickness=THICKNESS_WIDE, color=BLUE),
        AdditionalLine(6, 1, (2,), color=BLUE),
        AdditionalLine(1, 4, (5,), color=BLUE),
        AdditionalLine(4, 6, (0,), color=BLUE),
    ),
)
