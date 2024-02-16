from math import cos, sin

from app_dataclasses import Matrix, Levels


def rotation_matrix(a: int, b: int, y: int) -> Matrix:
    """
    rotation matrix of a, b, y radians around x, y, z axes (respectively)
    """

    sa, ca = sin(a), cos(a)
    sb, cb = sin(b), cos(b)
    sy, cy = sin(y), cos(y)

    return Matrix((
        (cb * cy, -cb * sy, sb),
        (ca * sy + sa * sb * cy, ca * cy - sy * sa * sb, -cb * sa),
        (sy * sa - ca * sb * cy, ca * sy * sb + sa * cy, ca * cb),
    ))
