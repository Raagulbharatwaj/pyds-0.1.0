import unittest
from unittest.mock import patch
from io import StringIO
from pyds.quene import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_default_len(self):
        self.assertEqual(len(self.q), 0)
        self.q.flush()

    def test_enqueue(self):
        self.q.flush()
        self.q.enqueue(2)
        self.assertEqual(len(self.q), 1)

    def test_front(self):
        self.q.flush()
        self.q.enqueue(2)
        self.q.enqueue(6)
        self.assertEqual(self.q.front(), 2)

    def test_rear(self):
        self.q.flush()
        self.q.enqueue(2)
        self.q.enqueue(6)
        self.assertEqual(self.q.rear(), 6)

    def test_len(self):
        self.q.flush()
        for i in range(1, 100):
            self.q.enqueue(i)
            self.assertEqual(len(self.q), i)

    def test_dequeue(self):
        self.q.flush()
        self.q.enqueue(2)
        self.q.enqueue(3)
        for i in range(2):
            x = self.q.front()
            self.assertEqual(self.q.dequeue(), x)
        self.assertEqual(len(self.q), 0)

    def test_print(self):
        self.q.flush()
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue(4)
        expected_output = "2 3 4 \n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.q)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_typecasting(self):
        self.q.flush()
        self.q.enqueue(1)
        self.q.enqueue("xyz")
        self.assertIsInstance(self.q.front(), int)
        self.q.dequeue()
        self.assertIsInstance(self.q.front(), str)

    def tearDown(self):
        self.q.flush()


if __name__ == '__main__':
    unittest.main()
