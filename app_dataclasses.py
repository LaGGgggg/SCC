from dataclasses import dataclass


THICKNESS_DEFAULT = 4


@dataclass
class Matrix:
    matrix: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]


@dataclass
class Color:

    r: int
    g: int
    b: int

    def get(self) -> tuple[int, int, int]:
        return tuple((self.r, self.g, self.b))


@dataclass
class Thickness:
    thickness: int


@dataclass
class AdditionalLine:

    start_vertice: int  # index
    end_vertice: int  # index
    faces: tuple[int, ...]  # indexes of faces WITHOUT start vertice
    is_faces_inverted: bool = False
    thickness: int = THICKNESS_DEFAULT
    color: Color | None = None
    is_always_hided: bool = False
    is_with_arrow: bool = False
    is_always_visible: bool = False


@dataclass
class Figures:
    figures: list  # list of the Figure class (help_classes/Figure)


@dataclass
class Texts:
    texts: list[str]


@dataclass
class Level:

    figures: Figures
    texts: Texts


@dataclass
class Levels:
    levels: dict[int, Level]
