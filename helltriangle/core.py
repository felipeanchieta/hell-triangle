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
    max_sum = 0
    max_col = 0  # Column index for the maximum next cell of each step

    if len(triangle) == 0:
        return 0

    for row in range(0, len(triangle) - 1):
        max_sum += triangle[row][max_col]

        # Choose between the left, right neighbours which one is the largest
        if triangle[row + 1][max_col] < triangle[row + 1][max_col + 1]:
            max_col += 1

    max_sum += triangle[len(triangle) - 1][max_col]
    return max_sum
