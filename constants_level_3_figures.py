from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
THICKNESS_DEFAULT = 4

__PRISM_HEIGHT = 1
__PRISM_SIDE = 3

PRISM_1 = Figure(
    vertices=(
        # bottom:
        (0, 0, -3),  # 0
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * -0.5, -3),  # 1
        (__PRISM_SIDE * 3**0.5, 0, -3),  # 2
        (__PRISM_SIDE * 3**0.5, __PRISM_SIDE, -3),  # 3
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * 1.5, -3),  # 4
        (0, __PRISM_SIDE, -3),  # 5
        # top:
        (0, 0, __PRISM_HEIGHT),  # 6
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * -0.5, __PRISM_HEIGHT),  # 7
        (__PRISM_SIDE * 3**0.5, 0, __PRISM_HEIGHT),  # 8
        (__PRISM_SIDE * 3**0.5, __PRISM_SIDE, __PRISM_HEIGHT),  # 9
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * 1.5, __PRISM_HEIGHT),  # 10
        (0, __PRISM_SIDE, __PRISM_HEIGHT),  # 11
    ),
    vertices_names=('F', 'E', 'D', 'C', 'B', 'A', 'F↓1', 'E↓1', 'D↓1', 'C↓1', 'B↓1', 'A↓1'),
    faces=(
        # counterclockwise:
        (6, 7, 8, 9, 10, 11),
        (5, 4, 3, 2, 1, 0),
        (0, 1, 7, 6),
        (1, 2, 8, 7),
        (2, 3, 9, 8),
        (3, 4, 10, 9),
        (4, 5, 11, 10),
        (11, 5, 0, 6),
    ),
    additional_lines=(
        AdditionalLine(5, 6, (4,), color=BLUE),
        AdditionalLine(6, 9, (1,), color=BLUE),
        AdditionalLine(9, 4, (2,), color=BLUE),
    ),
    faces_vertices_special_colors=(
        (1, ((4, 5, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (6, ((4, 5, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)

PRISM_2 = Figure(
    vertices=(
        # bottom:
        (0, 0, -3),  # 0
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * -0.5, -3),  # 1
        (__PRISM_SIDE * 3**0.5, 0, -3),  # 2
        (__PRISM_SIDE * 3**0.5, __PRISM_SIDE, -3),  # 3
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * 1.5, -3),  # 4
        (0, __PRISM_SIDE, -3),  # 5
        # top:
        (0, 0, __PRISM_HEIGHT),  # 6
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * -0.5, __PRISM_HEIGHT),  # 7
        (__PRISM_SIDE * 3**0.5, 0, __PRISM_HEIGHT),  # 8
        (__PRISM_SIDE * 3**0.5, __PRISM_SIDE, __PRISM_HEIGHT),  # 9
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * 1.5, __PRISM_HEIGHT),  # 10
        (0, __PRISM_SIDE, __PRISM_HEIGHT),  # 11
        # additional vertices:
        (0, __PRISM_SIDE, __PRISM_HEIGHT * 1.2 + 1),  # 12
        (0, __PRISM_SIDE * -0.2, -3),  # 13
        (__PRISM_SIDE * 3**0.5 * 1.2, __PRISM_SIDE, -3),  # 14
    ),
    vertices_names=('F', 'E', 'D', 'C', 'B', 'A', 'F↓1', 'E↓1', 'D↓1', 'C↓1', 'B↓1', 'A↓1', 'z', 'x', 'y'),
    faces=(
        # counterclockwise:
        (6, 7, 8, 9, 10, 11),
        (5, 4, 3, 2, 1, 0),
        (0, 1, 7, 6),
        (1, 2, 8, 7),
        (2, 3, 9, 8),
        (3, 4, 10, 9),
        (4, 5, 11, 10),
        (11, 5, 0, 6),
    ),
    additional_lines=(
        AdditionalLine(11, 12, (1, 4), is_with_arrow=True),
        AdditionalLine(0, 13, (0,), is_with_arrow=True),
        AdditionalLine(3, 14, (7,), is_with_arrow=True),
        AdditionalLine(3, 5, (0,)),
        AdditionalLine(5, 6, (4,), color=BLUE),
        AdditionalLine(6, 9, (1,), color=BLUE),
        AdditionalLine(9, 4, (2,), color=BLUE),
    ),
    faces_vertices_special_colors=(
        (1, ((4, 5, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (6, ((4, 5, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)
