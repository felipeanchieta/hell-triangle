from typing import List

Triangle = List[List[int]]


def max_sum_triangle(triangle: Triangle) -> int:
    """Returns the maximum sum of a triangle.

    Args:
        triangle: a triangle made up by lists of lists of integers.

    Returns:
        The maximum sum of a triangle.

    Examples:
        >>> max_sum_triangle([])
        0
        >>> max_sum_triangle([1, [2, 3]])
        4
        >>> max_sum_triangle([1, [2, 3], [4, 5, 6]])
        10

    """

    def aux(triangle: Triangle, summation: int = 0, index: int = 0) -> int:
        if len(triangle) == 0:
            return summation
        elif len(triangle) == 1:
            return summation + triangle[0][index]
        else:
            return max(aux(triangle[1:], summation + triangle[0][index], index),
                       aux(triangle[1:], summation + triangle[0][index], index + 1))

    return aux(triangle)
