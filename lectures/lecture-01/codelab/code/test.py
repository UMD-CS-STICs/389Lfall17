"""CMSC389L: Codelab 1"""
import unittest

import functions


class TestFooBarFlip(unittest.TestCase):
    def test_foo(self):
        self.assertEqual('bar', functions.foobar_flip('foo'))

    def test_foo(self):
        self.assertEqual('foo', functions.foobar_flip('bar'))


class TestStringCompress(unittest.TestCase):
    def test_empty(self):
        self.assertEqual('', functions.string_compress(None))

    def test_empty(self):
        self.assertEqual('', functions.string_compress(''))

    def test_length_one(self):
        self.assertEqual('a1', functions.string_compress('a'))

    def test_multiple_chars(self):
        self.assertEqual('a1b1c1d1', functions.string_compress('abcd'))

    def test_repeated_chars(self):
        self.assertEqual('a1b4c2d1e3', functions.string_compress('abbbbccdeee'))


class TestFibonacci(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(0, functions.fibonacci(0))
        self.assertEqual(1, functions.fibonacci(1))

    def test_small_numbers(self):
        answers = [2, 3, 5, 8, 13, 21, 34]
        for answer, n in zip(answers, range(3, 10)):
            self.assertEqual(answer, functions.fibonacci(n))

    # Optional Test
    def test_large_numbers(self):
        self.assertEqual(102334155, functions.fibonacci(40))
        self.assertEqual(1548008755920, functions.fibonacci(60))
        self.assertEqual(222232244629420445529739893461909967206666939096499764990979600, functions.fibonacci(300))


if __name__ == '__main__':
    unittest.main()
