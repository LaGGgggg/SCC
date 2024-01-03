from app_dataclasses import AdditionalLine, Color, Thickness
from help_classes import Figure


BLUE = Color(0, 0, 255)
THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

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
        # additional vertices:
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE / 2, -3),  # 12
    ),
    vertices_names=('F', 'E', 'D', 'C', 'B', 'A', 'F↓1', 'E↓1', 'D↓1', 'C↓1', 'B↓1', 'A↓1', 'E↓1'),
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
        AdditionalLine(1, 10, (0,), is_always_hided=True),
        AdditionalLine(1, 9, (0,), is_always_hided=True),
    ),
    faces_vertices_special_colors=(
        (0, ((10, 9, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (5, ((10, 9, BLUE, Thickness(THICKNESS_DEFAULT)),)),
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
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE * 1.5 * 1.2, -3),  # 12
        (__PRISM_SIDE * 3**0.5 * 1.2, __PRISM_SIDE / 2, -3),  # 13
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE / 2, -3),  # 14
        (__PRISM_SIDE * 3**0.5, __PRISM_SIDE / 2, -3),  # 15
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE / 2, __PRISM_HEIGHT * 1.8),  # 16
        # invisible:
        (0, __PRISM_SIDE / 2, -3),  # 17
        (__PRISM_SIDE * (3**0.5 / 2), __PRISM_SIDE / 2, __PRISM_HEIGHT),   # 18
    ),
    vertices_names=('F', 'E', 'D', 'C', 'B', 'A', 'F↓1', 'E↓1', 'D↓1', 'C↓1', 'B↓1', 'A↓1', 'x', 'y', 'E↓1', 'O', 'z'),
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
        AdditionalLine(4, 12, (0,), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(15, 13, (7,), is_with_arrow=True, thickness=THICKNESS_WIDE),
        AdditionalLine(17, 14, (0,), thickness=THICKNESS_WIDE),
        AdditionalLine(14, 15, (0,), thickness=THICKNESS_WIDE),
        AdditionalLine(4, 1, (0,), thickness=THICKNESS_WIDE),
        AdditionalLine(18, 14, (0,), is_always_hided=True, thickness=THICKNESS_WIDE),
        AdditionalLine(18, 16, (1,), thickness=THICKNESS_WIDE, is_with_arrow=True),
        AdditionalLine(1, 10, (0,), is_always_hided=True),
        AdditionalLine(1, 9, (0,), is_always_hided=True),
    ),
    faces_vertices_special_colors=(
        (0, ((10, 9, BLUE, Thickness(THICKNESS_DEFAULT)),)),
        (5, ((10, 9, BLUE, Thickness(THICKNESS_DEFAULT)),)),
    ),
)
