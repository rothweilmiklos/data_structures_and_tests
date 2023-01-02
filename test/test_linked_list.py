import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()
        self.l.add_to_end(4)
        self.l.add_to_beginning(3)
        self.l.add_to_end(5)
        self.l.add_to_beginning(2)
        self.l.add_to_end(6)
        self.l.add_to_end(7)
        self.l.add_to_beginning(1)

    def test_add_both_sides(self):
        self.assertEqual(self.l.head.value, 1)
        self.assertIsNotNone(self.l.head.next)
        self.assertEqual(self.l.tail.value, 7)
        self.assertEqual(self.l.tail.next, None)

    def test_count(self):
        self.assertEqual(self.l.count_elements(), 7)

    def test_delete_head(self):
        self.l.delete_at_index(0)

        self.assertEqual(self.l.head.value, 2)
        self.assertEqual(self.l.tail.value, 7)
        self.assertEqual(self.l.count_elements(), 6)
        self.assertIsNotNone(self.l.head.next)
        self.assertIsNone(self.l.tail.next)

    def test_delete_tail(self):
        self.l.delete_at_index(6)

        self.assertEqual(self.l.head.value, 1)
        self.assertEqual(self.l.tail.value, 6)
        self.assertEqual(self.l.count_elements(), 6)
        self.assertIsNotNone(self.l.head.next)
        self.assertIsNone(self.l.tail.next)

    def test_delete_middle(self):
        self.l.delete_at_index(1)

        self.assertEqual(self.l.head.value, 1)
        self.assertEqual(self.l.tail.value, 7)
        self.assertEqual(self.l.count_elements(), 6)

    def test_multiple_delete(self):
        self.l.delete_at_index(0)
        self.l.delete_at_index(5)
        self.l.delete_at_index(1)

        self.assertEqual(self.l.head.value, 2)
        self.assertEqual(self.l.tail.value, 6)
        self.assertEqual(self.l.count_elements(), 4)

    def test_delete_index_out_of_range(self):
        self.assertEqual(self.l.delete_at_index(7), -1)
        self.assertEqual(self.l.delete_at_index(-1), -1)


if __name__ == '__main__':
    unittest.main()

