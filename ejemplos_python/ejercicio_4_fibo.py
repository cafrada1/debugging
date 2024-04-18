import unittest


def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 2)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 3)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 5)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 8)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(6), 13)
