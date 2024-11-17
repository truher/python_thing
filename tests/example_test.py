import unittest

from example_package_truher import example


class ExampleTest(unittest.TestCase):
    def test_example(self) -> None:
        x = example.add_one(1)
        self.assertEqual(2, x)
