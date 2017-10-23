from unittest import TestCase

from helltriangle import core


class HellTriangleTest(TestCase):
    def test_regular_input(self) -> None:
        """
        Tests some regular inputs.
        """
        triangle_0 = [[6]]
        triangle_1 = [[6],
                      [3, 5]]
        triangle_2 = [[6],
                      [3, 5],
                      [9, 7, 1]]
        triangle_3 = [[6],
                      [3, 5],
                      [9, 7, 1],
                      [4, 6, 8, 4]]
        triangle_4 = [[6],
                      [3, 5],
                      [9, 7, 1],
                      [4, 6, 8, 4],
                      [2000, 0, 0, -10, 5]]

        self.assertEqual(6, core.max_sum_triangle(triangle_0))
        self.assertEqual(11, core.max_sum_triangle(triangle_1))
        self.assertEqual(18, core.max_sum_triangle(triangle_2))
        self.assertEqual(26, core.max_sum_triangle(triangle_3))
        self.assertEqual(26, core.max_sum_triangle(triangle_4))

    def test_empty_triangle(self) -> None:
        """
        Validate the neutral principle of summation
        """
        self.assertEqual(0, core.max_sum_triangle([]))
