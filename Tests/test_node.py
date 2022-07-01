import unittest
from pyds.node import ListNode, DoubleListNode, TreeNode


class TestNode(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_node_init(self):
        n = ListNode()
        self.assertIsNone(n["data"])
        self.assertIsNone(n["next"])

    def test_list_node_init_with_data(self):
        n = ListNode(3)
        self.assertIsNotNone(n["data"])
        self.assertEqual(n["data"], 3)
        self.assertIsNone(n["next"])

    def test_list_node_init_with_data_and_next(self):
        n  = ListNode(3)
        n1 = ListNode(4)
        n["next"] = n1
        self.assertIsNotNone(n["data"])
        self.assertIsNotNone(n["next"])
        self.assertEqual(n["data"], 3)
        self.assertEqual(n["next"], n1)
        self.assertIsInstance(n["next"], type(n))
        self.assertIsNotNone(n1["data"])
        self.assertEqual(n1["data"], 4)
        self.assertIsNone(n1["next"])

    def test_double_node_init(self):
        n = DoubleListNode()
        self.assertIsNone(n["data"])
        self.assertIsNone(n["next"])
        self.assertIsNone(n["prev"])

    def test_double_node_init_with_data(self):
        n = DoubleListNode(3)
        self.assertIsNotNone(n["data"])
        self.assertEqual(n["data"], 3)
        self.assertIsNone(n["next"])
        self.assertIsNone(n["prev"])

    def test_list_node_init_with_data_next_and_prev(self):
        n  = DoubleListNode(data=3)
        n1 = DoubleListNode(data=4, prev=n)
        n["next"] = n1
        self.assertIsNotNone(n["data"])
        self.assertIsNotNone(n["next"])
        self.assertEqual(n["data"], 3)
        self.assertEqual(n["next"], n1)
        self.assertIsNone(n["prev"])
        self.assertIsInstance(n["next"], type(n))
        self.assertIsInstance(n1["prev"], type(n1))
        self.assertIsNotNone(n1["data"])
        self.assertEqual(n1["data"], 4)
        self.assertEqual(n1["prev"], n)
        self.assertIsNone(n1["next"])

    def test_tree_node_init(self):
        t = TreeNode()
        self.assertIsNone(t["data"])
        self.assertIsNone(t["left"])
        self.assertIsNone(t["right"])

    def test_tree_node_init_with_data(self):
        t = TreeNode(data=3)
        self.assertIsNotNone(t["data"])
        self.assertIsNone(t["left"])
        self.assertIsNone(t["right"])
        self.assertEqual(t["data"], 3)

    def test_tree_node_init_with_data_and_left_and_right(self):
        t = TreeNode(data=3)
        left  = TreeNode(data=2)
        right = TreeNode(data=4)
        t["left"] = left
        t["right"] = right

        self.assertIsNotNone(t["data"])
        self.assertIsNotNone(t["left"])
        self.assertIsNotNone(t["right"])
        self.assertIsNone(left["left"])
        self.assertIsNone(left["right"])
        self.assertIsNone(right["left"])
        self.assertIsNone(right["right"])
        self.assertEqual(t["data"], 3)
        self.assertEqual(t["left"], left)
        self.assertEqual(t["right"], right)
        self.assertEqual(left["data"], 2)
        self.assertEqual(right["data"], 4)
        self.assertIsInstance(t["left"], TreeNode)
        self.assertIsInstance(t["right"],TreeNode)


if __name__ == '__main__':
    unittest.main()
