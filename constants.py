from app_dataclasses import Color, AdditionalLine, Figures, Texts, Level, Levels
from help_classes import Figure
import constants_level_1_figures, constants_level_2_figures, constants_level_3_figures, constants_level_4_figures
import constants_level_5_figures, constants_level_6_figures, constants_level_7_figures, constants_level_8_figures
import constants_level_9_figures, constants_level_10_figures, constants_level_11_figures, constants_level_12_figures

X, Y, Z = 0, 1, 2

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 128, 128)
BLUE = Color(0, 0, 255)
VIOLET = Color(174, 0, 255)

THICKNESS_DEFAULT = 4
THICKNESS_WIDE = 5

__CUBE_SIDE = 4

CUBE = Figure(
    vertices=(
        (0, 0, 0), (__CUBE_SIDE, 0, 0), (__CUBE_SIDE, __CUBE_SIDE, 0), (0, __CUBE_SIDE, 0), (0, 0, __CUBE_SIDE),
        (__CUBE_SIDE, 0, __CUBE_SIDE), (__CUBE_SIDE, __CUBE_SIDE, __CUBE_SIDE), (0, __CUBE_SIDE, __CUBE_SIDE),
        (-2, -2, -2), (-3, -3, -3),
    ),
    vertices_names=('A', 'B', 'C', 'D', 'A1', 'B1', 'C1', 'D1'),
    faces=(
        (0, 1, 2, 3),  # A1B1C1D1
        (5, 4, 7, 6),  # ABCD
        (4, 0, 3, 7),  # AA1DD1
        (1, 5, 6, 2),  # BB1CC1
        (4, 5, 1, 0),  # DD1CC1
        (3, 2, 6, 7),  # AA1BB1
    ),
    additional_lines=(
        AdditionalLine(1, 9, [1, 2, 5]),
    )
)

CUBE_2 = Figure(
    vertices=(
        (0, 0, 0), (__CUBE_SIDE, 0, 0), (__CUBE_SIDE, __CUBE_SIDE, 0), (0, __CUBE_SIDE, 0), (0, 0, __CUBE_SIDE),
        (__CUBE_SIDE, 0, __CUBE_SIDE), (__CUBE_SIDE, __CUBE_SIDE, __CUBE_SIDE), (0, __CUBE_SIDE, __CUBE_SIDE),
    ),
    vertices_names=('A', 'B', 'C', 'D', 'A1', 'B1', 'C1', 'D1'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (1, 5, 6, 2),
        (4, 5, 1, 0),
        (3, 2, 6, 7),
    ),
    additional_lines=(
        AdditionalLine(0, 5, [0]),
        AdditionalLine(1, 4, [1]),
        AdditionalLine(3, 5, [3], True),
        AdditionalLine(3, 6, [3]),
    ),
)

__PRISM_SIDE = 2
__PRISM_HEIGHT = 3

PRISM = Figure(
    vertices=(
        (0, 0, 0), (0, __PRISM_HEIGHT, 0), (3**0.5 / 2 * __PRISM_SIDE, __PRISM_HEIGHT, 0.5 * __PRISM_SIDE),
        (3**0.5 / 2 * __PRISM_SIDE, 0, 0.5 * __PRISM_SIDE), (0, 0, __PRISM_SIDE), (0, __PRISM_HEIGHT, __PRISM_SIDE),
    ),
    vertices_names=('A', 'B', 'C', 'A1', 'B1', 'C1'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 3, 2),
        (4, 0, 3),
        (1, 5, 2),
        (4, 5, 1, 0),
    ),
)

PRISM_MODDED = Figure(
    vertices=(
        (0, 0, 0), (0, __PRISM_HEIGHT, 0), (3**0.5 / 2 * __PRISM_SIDE, __PRISM_HEIGHT, 0.5 * __PRISM_SIDE),
        (3**0.5 / 2 * __PRISM_SIDE, 0, 0.5 * __PRISM_SIDE), (0, 0, __PRISM_SIDE), (0, __PRISM_HEIGHT, __PRISM_SIDE),
        (-2, -2, -2),
    ),
    vertices_names=('A', 'B', 'C', 'A1', 'B1', 'C1'),
    faces=(
        (0, 1, 2, 3),
        (5, 4, 3, 2),
        (4, 0, 3),
        (1, 5, 2),
        (4, 5, 1, 0),
    ),
    additional_lines=(
        AdditionalLine(0, 6, [1, 3]),
    ),
)

LEVELS = Levels({
    1: Level(
        Figures([
            constants_level_1_figures.PRISM_1,
            constants_level_1_figures.PRISM_2,
        ]),
        Texts([
            'В правильной четырёхугольный призме ABCDA↓1B↓1C↓1D↓1 сторона основания равна 12,'
            ' а боковое ребро равно пять найдите угол между прямыми AC и BC↓1.',
            'Введём прямоугольную систему координат с началом в точке B, найдём координаты точек A(12; 0; 0) и'
            ' C(0; 12; 0), B(0; 0; 0) и C↓1(0; 12; 5), а также векторов и тогда косинус угла θ равен:'
            ' cosθ = {%render_image#static/level_1/1.png%} = {%render_image#static/level_1/2.png%} ='
            ' {%render_image#static/level_1/3.png%} => искомый угол θ между прямыми AC и BC1 равен'
            ' {%render_image#static/level_1/4.png%}.',
        ]),
    ),
    2: Level(
        Figures([
            constants_level_2_figures.PYRAMID_1,
            constants_level_2_figures.PYRAMID_2,
        ]),
        Texts([
            'В правильной шестиугольной пирамиде SABCDEF с основанием ABCDEF сторона основания равна 2,'
            ' а боковое ребро равно 4. Точка M – середина SE. Найдите угол между прямыми SB и CM.',
            ' Введём прямоугольную систему координат с началом в точке B. Найдём координаты точек B(0; 0; 0) и'
            ' {%render_image#static/level_2/1.png%}, {%render_image#static/level_2/2.png%} и'
            ' {%render_image#static/level_2/3.png%}, а также векторов {%render_image#static/level_2/4.png%} и'
            ' {%render_image#static/level_2/5.png%}. Тогда косинус искомого угла θ равен: cosθ ='
            ' {%render_image#static/level_2/6.png%} = {%render_big_image#static/level_2/7_big.png%} ='
            ' {%render_image#static/level_2/8.png%}. Следовательно, искомый угол θ между прямыми SB и CM равен'
            ' {%render_image#static/level_2/9.png%}'
        ]),
    ),
    3: Level(
        Figures([
            constants_level_3_figures.PRISM_1,
            constants_level_3_figures.PRISM_2,
            constants_level_3_figures.PRISM_2,
            constants_level_3_figures.PRISM_2,
        ]),
        Texts([
            'В правильной шестиугольной призме ABCDEFA↓1B↓1C↓1D↓1E↓1F↓1 сторона основания равна 3, а высота равна 1.'
            ' Найдите угол между прямой F↓1B↓1 и плоскостью AF↓1C↓1.',
            'Введём прямоугольную систему координат с началом в точке A. Найдём вначале координаты точек'
            ' {%render_image#static/level_3/1.png%}, F↓1(3; 0; 1) и вектора {%render_image#static/level_3/2.png%}.'
            ' Найдём далее координаты точек A(0, 0, 0), {%render_image#static/level_3/3.png%} и векторов'
            ' {%render_image#static/level_3/4.png%}, {%render_image#static/level_3/5.png%}.',
            'Найдём наконец координаты {a; b; c} вектора {%render_small_image#static/level_3/6_small.png%},'
            ' перпендикулярного плоскости (AF↓1C↓1), из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_3/6_small.png%} с векторами'
            ' {%render_small_image#static/level_3/7_small.png%} и {%render_small_image#static/level_3/8_small.png%}'
            ' получаем систему уравнений: {%render_image#static/level_3/9.png%} ≡'
            ' {%render_image#static/level_3/10.png%} ≡ {%render_image#static/level_3/11.png%}',
            'Эта система имеет бесконечное множество решений. Соответственно все векторы с координатами'
            ' {%render_image#static/level_3/12.png%}, где b {%render_small_image#static/level_3/18_small.png%} R и'
            ' b ≠ 0 (поскольку нормальный вектор по определению не нулевой),'
            ' перпендикулярной плоскостью выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_3/6_small.png%} положив b = 1. Тогда'
            ' {%render_small_image#static/level_3/6_small.png%} = {%render_image#static/level_3/13.png%}.'
            ' Таким образом синус угла между прямой F↓1B↓1 и плоскостью (AF↓1C↓1) равен: sinθ ='
            ' {%render_image#static/level_3/14.png%} = {%render_big_image#static/level_3/15_big.png%} ='
            ' {%render_image#static/level_3/16.png%}. Тогда искомый угол θ между прямой и плоскостью равен'
            ' {%render_image#static/level_3/17.png%}',
        ]),
    ),
    4: Level(
        Figures([
            constants_level_4_figures.PYRAMID_1,
            constants_level_4_figures.PYRAMID_2,
            constants_level_4_figures.PYRAMID_2,
        ]),
        Texts([
            'В правильной треугольной пирамиде SABC с основанием ABC сторона основания равна 2, а боковое ребро равно'
            ' 3. Найдите угол между плоскостью BSC и прямой MN, где точка N – середина ребра AC, а точка M лежит на'
            ' ребре SB так, что BM = 1.',
            'Введём прямоугольную систему координат с началом в точке N. Тогда BN ='
            ' {%render_small_image#static/level_4/1_small.png%}, ON = {%render_image#static/level_4/2.png%}, OB ='
            ' {%render_image#static/level_4/3.png%}, SO = {%render_image#static/level_4/4.png%} ='
            ' {%render_image#static/level_4/5.png%}. Значит, можно довольно легко найти координаты точек N(0; 0; 0),'
            ' {%render_image#static/level_4/6.png%} и вектора {%render_small_image#static/level_4/7_small.png%} ='
            ' {%render_image#static/level_4/8.png%}. Также можно найти координаты точек'
            ' {%render_image#static/level_4/9.png%}, {%render_image#static/level_4/10.png%}, C(1; 0; 0) и векторов'
            ' {%render_small_image#static/level_4/11_small.png%} = {%render_image#static/level_4/12.png%},'
            ' {%render_small_image#static/level_4/13_small.png%} = {%render_image#static/level_4/14.png%}.',
            'Найдём координаты {a; b; c} вектора {%render_small_image#static/level_4/15_small.png%}, перпендикулярного'
            ' плоскости BSC. Они ищутся из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_4/15_small.png%} с векторами'
            ' {%render_small_image#static/level_4/11_small.png%} и {%render_small_image#static/level_4/13_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_4/16.png%} ≡'
            ' {%render_image#static/level_4/17.png%} ≡ {%render_image#static/level_4/18.png%} Эта система имеет'
            ' бесконечное множество решений. Соответственно, все векторы с координатами'
            ' {%render_image#static/level_4/19.png%}, где c  {%render_small_image#static/level_4/20_small.png%} R и'
            ' c ≠ 0, перпендикулярны плоскости BSC. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_4/15_small.png%}, положив c = 2. Тогда'
            ' {%render_small_image#static/level_4/15_small.png%} = {%render_image#static/level_4/21.png%}.'
            ' Таким образом, синус угла θ между прямой MN и плоскостью BSC равен: sinθ ='
            ' {%render_image#static/level_4/22.png%} = {%render_big_image#static/level_4/23_big.png%} ='
            ' {%render_image#static/level_4/24.png%}. Тогда искомый угол θ между прямой и плоскостью равен'
            ' {%render_image#static/level_4/25.png%}',
        ]),
    ),
    5: Level(
        Figures([
            constants_level_5_figures.PRISM_4_1,
            constants_level_5_figures.PRISM_4_2,
        ]),
        Texts([
            'В правильной четырёхугольной призме ABCDA↓1B↓1C↓1D↓1 сторона основания равна 3, а боковое ребро равно'
            ' 5. На ребре AA↓1 взята точка M так, что AM = 2. На ребре BB↓1 взята точка K так, что B↓1K = 2. Найдите'
            ' угол между плоскостями CC↓1D↓1 и D↓1MK.',
            'Введём прямоугольную систему координат с началом в точке B. Поскольку плоскость CC↓1 D↓1 параллельна'
            ' плоскости xOz, то её нормальным вектором является вектор'
            ' {%render_small_image#static/level_5/1_small.png%}↓1 = {0; 1; 0}. Продлив прямые KM и NK до пересечения их'
            ' соответственно с осями Ox и Oy, легко найти длины отрезков, отсекаемых плоскостью D↓1 MK на осях от'
            ' начала системы координат. Тогда уравнение плоскости D↓1 MK в “отрезках” имеет вид:'
            ' {%render_image#static/level_5/2.png%} = 1. Отсюда получим общее уравнение плоскости D↓1 MK: x-3y+3z-9=0.'
            ' Следовательно, нормальным вектором плоскости D↓1 MK является вектор'
            ' {%render_small_image#static/level_5/1_small.png%}↓2 = {1; -3; 3}. Таким образом, косинус угла θ между'
            ' плоскостями CC↓1 D↓1 и D↓1 MK равен: cosθ = {%render_image#static/level_5/3.png%} ='
            ' {%render_image#static/level_5/4.png%} = {%render_image#static/level_5/5.png%}. Следовательно, искомый'
            ' угол θ равен {%render_image#static/level_5/6.png%}',
        ]),
    ),
    6: Level(
        Figures([
            constants_level_6_figures.PYRAMID_1,
            constants_level_6_figures.PYRAMID_2,
            constants_level_6_figures.PYRAMID_2,
            constants_level_6_figures.PYRAMID_2,
            constants_level_6_figures.PYRAMID_2,
        ]),
        Texts([
            'Все рёбра треугольной пирамиды SABC равны между собой. Точки K и L – середины рёбер AB и AC'
            ' соответственно. Найдите угол между плоскостями ABS и KSL.',
            'Введём прямоугольную систему координат с началом в точке K. Пусть длина ребра пирамиды равна m. Тогда'
            ' SK = CK = {%render_image#static/level_6/1.png%}, OK = {%render_image#static/level_6/2.png%} ='
            ' {%render_image#static/level_6/3.png%}, SO = {%render_image#static/level_6/4.png%} ='
            ' {%render_image#static/level_6/5.png%}. Значит, можно найти координаты точек:'
            ' {%render_image#static/level_6/6.png%}, {%render_image#static/level_6/7.png%},'
            ' {%render_image#static/level_6/8.png%} и векторов {%render_small_image#static/level_6/9_small.png%} ='
            ' {%render_image#static/level_6/10.png%}, {%render_small_image#static/level_6/12_small.png%} ='
            ' {%render_image#static/level_6/13.png%}, {%render_small_image#static/level_6/14_small.png%} ='
            ' {%render_image#static/level_6/15.png%}.',
            'Найдём координаты векторов'
            ' {%render_small_image#static/level_6/16_small.png%}↓1 и'
            ' {%render_small_image#static/level_6/16_small.png%}↓2, перпендикулярных соответственно плоскостям'
            ' ABS и KSL. Начнём с вектора'
            ' {%render_small_image#static/level_6/16_small.png%}↓1 = {a; b; c}. Его координаты ищутся из условий'
            ' равенства нулю скалярных произведений {%render_small_image#static/level_6/16_small.png%}↓1 с векторами'
            ' {%render_small_image#static/level_6/9_small.png%} и {%render_small_image#static/level_6/12_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_6/17.png%} ≡'
            ' {%render_big_image#static/level_6/18_big.png%} ≡ {%render_image#static/level_6/19.png%} Эта система имеет'
            ' бесконечное множество решений. Соответственно, все векторы с координатами'
            ' {%render_small_image#static/level_6/21_small.png%}, где c '
            '{%render_small_image#static/level_6/20_small.png%} R и'
            ' c ≠ 0, перпендикулярны плоскости ABS. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_6/16_small.png%}↓1, положив c = 1. Тогда'
            ' {%render_small_image#static/level_6/16_small.png%}↓1 ='
            ' {%render_small_image#static/level_6/22_small.png%}',
            'Найдём теперь координаты вектора {%render_small_image#static/level_6/16_small.png%}↓2 = {p; q; r},'
            ' перпендикулярного плоскости KSL. Его координаты ищутся из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_6/16_small.png%}↓2 с векторами'
            ' {%render_small_image#static/level_6/12_small.png%} и {%render_small_image#static/level_6/14_small.png%}'
            ' Получаем систему уравнений: {%render_image#static/level_6/23.png%} ≡'
            ' {%render_big_image#static/level_6/24_big.png%} ≡ {%render_image#static/level_6/25.png%} Эта система имеет'
            ' бесконечное множество решений. Соответственно, все векторы с координатами'
            ' {%render_image#static/level_6/26.png%}, где r {%render_small_image#static/level_6/20_small.png%} R и'
            ' r ≠ 0, перпендикулярны плоскости ABS. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_6/16_small.png%}↓2, положив r = 1. Тогда'
            ' {%render_small_image#static/level_6/16_small.png%}↓2 = {%render_image#static/level_6/27.png%}',
            'Таким'
            ' образом, косинус угла θ между плоскостями ABS и KSL равен: cosθ = {%render_image#static/level_6/28.png%}'
            ' = {%render_big_image#static/level_6/29_big.png%} = {%render_image#static/level_6/30.png%}. Следовательно,'
            ' искомый угол θ между плоскостями ABS и KSL равен {%render_image#static/level_6/31.png%}',
        ]),
    ),
    7: Level(
        Figures([
            constants_level_7_figures.PRISM_1,
            constants_level_7_figures.PRISM_2,
        ]),
        Texts([
            'В правильной шестиугольной призме ABCDEFA↓1B↓1C↓1D↓1E↓1F↓1 сторона основания равна 3, а боковое ребро'
            ' равно 2. Найдите расстояние от точки E до прямой B↓1 C↓1',
            'Введём прямоугольную систему координат с началом в точке O. Найдём координаты точек E(3; 0; 0),'
            ' B↓1(-3; 0; 2), {%render_image#static/level_7/1.png%} и векторов'
            ' {%render_small_image#static/level_7/2_small.png%} = {6; 0; -2},'
            ' {%render_small_image#static/level_7/3_small.png%} = {%render_image#static/level_7/4.png%}. Вычислим'
            ' косинус угла θ между векторами {%render_small_image#static/level_7/2_small.png%} и'
            ' {%render_small_image#static/level_7/3_small.png%}: cosθ = {%render_image#static/level_7/5.png%} ='
            ' {%render_image#static/level_7/6.png%} = {%render_image#static/level_7/7.png%}. Найдём синус угла'
            ' θ: sinθ = {%render_small_image#static/level_7/8_small.png%} = {%render_image#static/level_7/9.png%}.'
            ' Вычислим расстояние'
            ' от точки E до прямой B↓1C↓1: p(E, B↓1 C↓1) = {%render_small_image#static/level_7/10_small.png%} ='
            ' {%render_image#static/level_7/11.png%} = {%render_small_image#static/level_7/12_small.png%}',
        ]),
    ),
    8: Level(
        Figures([
            constants_level_8_figures.PYRAMID_1,
            constants_level_8_figures.PYRAMID_2,
        ]),
        Texts([
            'В правильной четырёхугольной пирамиде SABCD с основанием ABCD сторона основания равна 2, а боковое ребро'
            ' равно 4. Точка M – середина SD. Найдите расстояние от точки A до прямой MB.',
            'Введём прямоугольную систему координат с началом в точке O. Найдём координаты точек: A(1; 1; 0),'
            ' B(1; -1; 0) и {%render_image#static/level_8/1.png%} (учитывая, что SO ='
            ' {%render_small_image#static/level_8/2_small.png%} = {%render_small_image#static/level_8/3_small.png%})'
            ' и векторов {%render_small_image#static/level_8/4_small.png%} = {0; 2; 0} и'
            ' {%render_small_image#static/level_8/5_small.png%} = {%render_image#static/level_8/6.png%}. Вычислим'
            ' косинус угла θ между векторами {%render_small_image#static/level_8/4_small.png%} и'
            ' {%render_small_image#static/level_8/5_small.png%}: cosθ = {%render_image#static/level_8/7.png%} ='
            ' {%render_big_image#static/level_8/8_big.png%} = {%render_image#static/level_8/9.png%}. Найдём синус'
            ' угла θ: sinθ = {%render_small_image#static/level_8/10_small.png%} ='
            ' {%render_image#static/level_8/11.png%}. Вычислим'
            ' расстояние от точки A до прямой MB: p(A, BM) = {%render_image#static/level_8/11.png%} ='
            ' {%render_image#static/level_8/12.png%} = {%render_image#static/level_8/13.png%}.',
        ]),
    ),
    9: Level(
        Figures([
            constants_level_9_figures.PRISM_4_1,
            constants_level_9_figures.PRISM_4_2,
            constants_level_9_figures.PRISM_4_2,
        ]),
        Texts([
            'В правильной четырёхугольной призме ABCDA↓1 B↓1 C↓1 D↓1 сторона основания равна 1, а боковое ребро равно'
            ' 2. Точка M – середина ребра AA↓1 . найдите расстояние от точки M до плоскости DA↓1 C↓1.',
            'Введём прямоугольную систему координат с началом в точке A. Найдём координаты точек: D(1; 0; 0),'
            ' A↓1(0; 0; 2), C↓1(1; 1; 2) и векторов {%render_small_image#static/level_9/1_small.png%} = {1; 0; -2},'
            ' {%render_small_image#static/level_9/2_small.png%} = {1; 1; 0}. Найдём координаты {a; b, c} вектора'
            ' {%render_small_image#static/level_9/3_small.png%}, перпендикулярного плоскости DA↓1 C↓1 , из условий'
            ' равенства нулю скалярных произведений {%render_small_image#static/level_9/3_small.png%} с векторами'
            ' {%render_small_image#static/level_9/1_small.png%} и {%render_small_image#static/level_9/2_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_9/4.png%} ≡ {%render_image#static/level_9/5.png%}'
            ' ≡ {%render_image#static/level_9/6.png%}',
            'Эта система имеет бесконечное множество решений. Соответственно,'
            ' все векторы с координатами {2c; -2c; c}, где c {%render_small_image#static/level_9/7_small.png%} R и'
            ' c ≠ 0, перпендикулярны плоскости DA↓1 C↓1. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_9/3_small.png%}, положив c = 1. Тогда'
            ' {%render_small_image#static/level_9/3_small.png%} = {2; -2; 1}. Найдём теперь координаты точки M(0; 0; 1)'
            ' и вектора {%render_small_image#static/level_9/8_small.png%} = {0; 0; 1}. Вычислим расстояние от точки'
            ' M до плоскости DA↓1C↓1: p(M, DA_1 C_1) = {%render_image#static/level_9/9.png%} ='
            ' {%render_image#static/level_9/10.png%} = {%render_image#static/level_9/11.png%}.',
        ]),
    ),
    10: Level(
        Figures([
            constants_level_10_figures.PYRAMID_1,
            constants_level_10_figures.PYRAMID_2,
            constants_level_10_figures.PYRAMID_2,
        ]),
        Texts([
            'В правильной шестиугольной пирамиде SABCDEF с основанием ABCDEF сторона основания равна 5, а боковое ребро'
            ' равно 8. Точка K – середина SB. Найдите расстояние от точки A до плоскости KDF.',
            'Введём прямоугольную систему координат с началом в точке O. Найдём координаты точек:'
            ' {%render_image#static/level_10/1.png%} (учитывая, что SO ='
            ' {%render_small_image#static/level_10/2_small.png%} = {%render_small_image#static/level_10/3_small.png%}),'
            ' D(-5; 0; 0), {%render_image#static/level_10/4.png%}'
            ' и векторов {%render_small_image#static/level_10/5_small.png%} = {%render_image#static/level_10/6.png%},'
            ' {%render_small_image#static/level_10/7_small.png%} = {%render_image#static/level_10/8.png%}. Найдём'
            ' координаты {a; b; c} вектора {%render_small_image#static/level_10/13_small.png%}, перпендикулярного'
            ' плоскости KDF, из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_10/13_small.png%} с векторами'
            ' {%render_small_image#static/level_10/5_small.png%} и {%render_small_image#static/level_10/7_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_10/9.png%} ≡'
            ' {%render_big_image#static/level_10/10_big.png%} ≡ {%render_image#static/level_10/11.png%}',
            'Эта система имеет бесконечное множество решений. Соответственно, все векторы с координатами'
            ' {%render_image#static/level_10/12.png%}, где a {%render_small_image#static/level_10/13_small.png%} R и'
            ' a ≠ 0, перпендикулярны плоскости KDF. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_10/13_small.png%}, положив a ='
            ' {%render_small_image#static/level_10/14_small.png%}. Тогда'
            ' {%render_small_image#static/level_10/13_small.png%} = {%render_image#static/level_10/15.png%}. Найдём'
            ' теперь координаты точки A(5; 0; 0) и вектора {%render_small_image#static/level_10/16_small.png%} ='
            ' {-10; 0; 0}. Вычислим расстояние от точки A до плоскости KDF: p(A, KDF) ='
            ' {%render_image#static/level_10/17.png%} = {%render_big_image#static/level_10/18_big.png%} ='
            ' {%render_image#static/level_10/19.png%}.',
        ]),
    ),
    11: Level(
        Figures([
            constants_level_11_figures.PRISM_3_1,
            constants_level_11_figures.PRISM_3_2,
            constants_level_11_figures.PRISM_3_2,
        ]),
        Texts([
            'В правильной треугольной призме ABCA↓1 B↓1 C↓1 сторона основания равна 1, а боковое ребро равно 3. Найдите'
            ' расстояние между прямыми AB↓1 и BC↓1.',
            'Введём прямоугольную систему координат с началом в точке O. Найдём координаты точек:'
            ' {%render_image#static/level_11/1.png%}, {%render_image#static/level_11/2.png%},'
            ' {%render_image#static/level_11/3.png%}, {%render_image#static/level_11/4.png%} и векторов'
            ' {%render_small_image#static/level_11/5_small.png%} = {%render_image#static/level_11/6.png%},'
            ' {%render_small_image#static/level_11/7_small.png%} = {%render_image#static/level_11/8.png%}.'
            ' Найдём координаты {a; b; c} вектора {%render_small_image#static/level_11/9_small.png%}, перпендикулярного'
            ' векторам {%render_small_image#static/level_11/5_small.png%} и'
            ' {%render_small_image#static/level_11/7_small.png%}, из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_11/9_small.png%} с векторами'
            ' {%render_small_image#static/level_11/5_small.png%} и {%render_small_image#static/level_11/7_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_11/10.png%} ≡'
            ' {%render_big_image#static/level_11/11_big.png%} ≡ {%render_image#static/level_11/12.png%}',
            'Эта система имеет бесконечное множество решений. Соответственно, все векторы с координатами {-6c; 0; c},'
            ' где c {%render_small_image#static/level_11/13_small.png%} R и c ≠ 0, перпендикулярны'
            ' {%render_small_image#static/level_11/5_small.png%} и {%render_small_image#static/level_11/7_small.png%}'
            ' Выберем из данного множества ненулевой вектор {%render_small_image#static/level_11/9_small.png%},'
            ' положив c = 1. Тогда {%render_small_image#static/level_11/9_small.png%} = {-6; 0; 1}. Найдём теперь'
            ' координаты вектора, началом которого служит любая точка прямой AB↓1, а концом – произвольная точка прямой'
            ' BC↓1 (например, вектора {%render_small_image#static/level_11/14_small.png%}):'
            ' {%render_small_image#static/level_11/14_small.png%} = {1; 0; 3}. Вычислим теперь расстояние между прямыми'
            ' AB↓1 и BC↓1: p(AB↓1, BC↓1) = {%render_image#static/level_11/15.png%} ='
            ' {%render_image#static/level_11/16.png%} = {%render_image#static/level_11/17.png%}.',
        ]),
    ),
    12: Level(
        Figures([
            constants_level_12_figures.PRISM_4_1,
            constants_level_12_figures.PRISM_4_2,
            constants_level_12_figures.PRISM_4_2,
        ]),
        Texts([
            'В правильной четырёхугольной пирамиде SABCD с основанием ABCD сторона основания равна 3, а боковое ребро'
            ' равно 4. Точка M – середина SB. Найдите расстояние между прямыми SA и MC.',
            'Введём прямоугольную систему координат с началом в точке O. Найдём координаты точек:'
            ' {%render_image#static/level_12/1.png%}, {%render_image#static/level_12/2.png%},'
            ' {%render_image#static/level_12/3.png%}, {%render_image#static/level_12/4.png%} и векторов:'
            ' {%render_small_image#static/level_12/5_small.png%} = {%render_image#static/level_12/6.png%},'
            ' {%render_small_image#static/level_12/7_small.png%} = {%render_image#static/level_12/8.png%}.'
            ' Найдём координаты {a; b; c} вектора {%render_small_image#static/level_12/9_small.png%}, перпендикулярного'
            ' векторам {%render_small_image#static/level_12/5_small.png%} и'
            ' {%render_small_image#static/level_12/7_small.png%} из условий равенства нулю скалярных произведений'
            ' {%render_small_image#static/level_12/9_small.png%} с векторами'
            ' {%render_small_image#static/level_12/5_small.png%} и {%render_small_image#static/level_12/7_small.png%}.'
            ' Получаем систему уравнений: {%render_image#static/level_12/10.png%} ≡'
            ' {%render_big_image#static/level_12/11_big.png%} ≡ {%render_image#static/level_12/12.png%}',
            'Эта система имеет бесконечное множество решений. Соответственно, все векторы с координатами'
            ' {%render_image#static/level_12/13.png%}, где c {%render_small_image#static/level_12/14_small.png%} R и'
            ' c ≠ 0, перпендикулярны {%render_small_image#static/level_12/5_small.png%} и'
            ' {%render_small_image#static/level_12/7_small.png%}. Выберем из данного множества ненулевой вектор'
            ' {%render_small_image#static/level_12/9_small.png%}, положив c = 3. Тогда,'
            ' {%render_small_image#static/level_12/9_small.png%} = {%render_small_image#static/level_12/15_small.png%}.'
            ' Найдём'
            ' теперь координаты вектора, началом которого служит любая точка прямой SA, а концом – произвольная точка'
            ' прямой MC (например, вектора {%render_small_image#static/level_12/16_small.png%}):'
            ' {%render_small_image#static/level_12/16_small.png%} ='
            ' {%render_small_image#static/level_12/17_small.png%}. Вычислим'
            ' расстояние между прямыми SA и MC: p(SA, MC) = {%render_image#static/level_12/18.png%} ='
            ' {%render_image#static/level_12/19.png%} = {%render_image#static/level_12/20.png%}.',
        ]),
    ),
})
