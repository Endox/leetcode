import timeit
import unittest
from solution_1361 import Solution


# noinspection PyMethodMayBeStatic
class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        assert Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]) is True

    def test_case_2(self):
        assert Solution().validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]) is False

    def test_case_3(self):
        assert Solution().validateBinaryTreeNodes(2, [1, 0], [-1, -1]) is False

    def test_case_4(self):
        assert Solution().validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]) is True

    def test_case_large(self):
        with open('large_test_case.txt', 'r') as f:
            n_str, left_child_str, right_child_str = f.readlines()
            n = int(n_str)
            left_child = eval(left_child_str)
            right_child = eval(right_child_str)

            assert Solution().validateBinaryTreeNodes(n, left_child, right_child) == True

            samples = 10
            seconds = timeit.timeit(lambda: Solution().validateBinaryTreeNodes(n, left_child, right_child), number=samples)
            print(f"Seconds elapsed: {seconds / samples}")


if __name__ == '__main__':
    unittest.main()
