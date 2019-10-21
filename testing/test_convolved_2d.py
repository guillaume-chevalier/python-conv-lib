from unittest import TestCase
import unittest
import itertools

from conv import convolved_2d


class TestConvolved2D(TestCase):

    def test_trivial_1x1_loop(self):
        base = tuple(tuple(range(i ** 2, 7 + i ** 2)) for i in range(7))
        expected = tuple(([i],) for i in itertools.chain(*base))
        result = []

        for kernel_hover in convolved_2d(base, kernel_size=1, padding=0, stride=1):
            result.append(tuple(kernel_hover))
        result = tuple(result)

        self.assertEqual(expected, result)

    def test_simple_2x2_loop_on_3x2(self):
        base = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        expected = (
            (
                [1, 2],
                [3, 4]
            ), (
                [3, 4],
                [5, 6]
            )
        )
        result = []

        for kernel_hover in convolved_2d(base, kernel_size=2, padding=0, stride=1):
            result.append(tuple(kernel_hover))
        result = tuple(result)

        print(result)
        print(expected)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
