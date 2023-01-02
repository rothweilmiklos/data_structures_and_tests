import unittest
from binary_search_tree import BinarySearchTreeNode


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.bsn = BinarySearchTreeNode()
        self.bsn.add_node(data=5)
        self.bsn.add_node(data=2)
        self.bsn.add_node(data=13)
        self.bsn.add_node(data=4)
        self.bsn.add_node(data=3)
        self.bsn.add_node(data=14)
        self.bsn.add_node(data=15)
        self.bsn.add_node(data=12)

    def test_add_node(self):
        # Test root and leaf values
        self.assertEqual(self.bsn.value, 5)
        self.assertEqual(self.bsn.left.right.left.value, 3)
        self.assertEqual(self.bsn.right.left.value, 12)
        self.assertEqual(self.bsn.right.right.right.value, 15)

        # Test subtree endings
        self.assertIsNone(self.bsn.left.left)
        self.assertIsNone(self.bsn.left.right.right)
        self.assertIsNone(self.bsn.left.right.left.left)
        self.assertIsNone(self.bsn.left.right.left.right)
        self.assertIsNone(self.bsn.right.left.left)
        self.assertIsNone(self.bsn.right.left.right)

    def test_search(self):
        # Test contained elements
        self.assertTrue(self.bsn.search(5))
        self.assertTrue(self.bsn.search(2))
        self.assertTrue(self.bsn.search(4))
        self.assertTrue(self.bsn.search(3))
        self.assertTrue(self.bsn.search(13))
        self.assertTrue(self.bsn.search(12))
        self.assertTrue(self.bsn.search(14))
        self.assertTrue(self.bsn.search(15))

        # Test not contained elements
        self.assertFalse(self.bsn.search(1))
        self.assertFalse(self.bsn.search(6))
        self.assertFalse(self.bsn.search(11))
        self.assertFalse(self.bsn.search(16))

    def test_get_max(self):
        self.assertEqual(self.bsn.get_max(), 15)

    def test_get_min(self):
        self.assertEqual(self.bsn.get_min(), 2)

    def test_in_order_traversal(self):
        self.assertEqual(self.bsn.in_order_traversal(), [2, 3, 4, 5, 12, 13, 14, 15])

    def test_pre_order_traversal(self):
        self.assertEqual(self.bsn.pre_order_traversal(), [5, 2, 4, 3, 13, 12, 14, 15])

    def test_post_order_traversal(self):
        self.assertEqual(self.bsn.post_order_traversal(), [3, 4, 2, 12, 15, 14, 13, 5])

    def test_delete_value(self):
        self.bsn.add_node(data=1)
        self.bsn.add_node(data=20)
        self.bsn.add_node(data=17)
        self.bsn.add_node(data=30)

        self.bsn.delete_value(13)
        self.assertFalse(self.bsn.search(13))

        self.bsn.delete_value(1)
        self.assertFalse(self.bsn.search(1))

        self.bsn.delete_value(20)
        self.assertFalse(self.bsn.search(20))


class TestEmptyBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_bsn = BinarySearchTreeNode()

    def test_search_in_empty_tree(self):
        self.assertFalse(self.empty_bsn.search(2))

    def test_get_max_in_empty_tree(self):
        self.assertIsNone(self.empty_bsn.get_max())

    def test_get_min_in_empty_tree(self):
        self.assertIsNone(self.empty_bsn.get_min())

    def test_traversal_in_order_in_empty_tree(self):
        self.assertEqual(self.empty_bsn.in_order_traversal(), [])

    def test_traversal_pre_order_in_empty_tree(self):
        self.assertEqual(self.empty_bsn.pre_order_traversal(), [])

    def test_traversal_post_order_in_empty_tree(self):
        self.assertEqual(self.empty_bsn.post_order_traversal(), [])

    def test_delete_value_in_empty_tree(self):
        self.assertIsNone(self.empty_bsn.delete_value(10))


if __name__ == '__main__':
    unittest.main()
