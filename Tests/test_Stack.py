import unittest
from unittest.mock import patch
from io import StringIO
from pyds.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.s1 = Stack()

    def test_default_len(self):
        self.assertEqual(len(self.s1), 0)
        self.s1.flush()

    def test_push(self):
        self.s1.flush()
        self.s1.push(2)
        self.assertEqual(len(self.s1), 1)

    def test_len(self):
        self.s1.flush()
        for i in range(1, 100):
            self.s1.push(i)
            self.assertEqual(len(self.s1), i)

    def test_top(self):
        self.s1.flush()
        self.s1.push(2)
        self.assertEqual(self.s1.top(), 2)

    def test_pop(self):
        self.s1.flush()
        self.s1.push(2)
        self.s1.push(3)
        for i in range(2):
            x = self.s1.top()
            self.assertEqual(self.s1.pop(), x)
        self.assertEqual(len(self.s1), 0)

    def test_print(self):
        self.s1.flush()
        self.s1.push(2)
        self.s1.push(3)
        self.s1.push(4)
        expected_output = "4 3 2 \n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.s1)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_typecasting(self):
        self.s1.flush()
        self.s1.push(1)
        self.s1.push("xyz")
        self.assertIsInstance(self.s1.top(), str, f"type given is{type(self.s1.top())}")
        self.s1.pop()
        self.assertIsInstance(self.s1.top(), int, f"type given is{type(self.s1.top())}")

    def tearDown(self):
        self.s1.flush()


if __name__ == '__main__':
    unittest.main()
