class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def add_to_end(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def add_to_beginning(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        new_element = Node(value, self.head)
        self.head = new_element

    def print_list(self):
        if self.head is None:
            print("Sorry the list is empty")
            return -1

        dummy_node = self.head
        text = ""
        while dummy_node is not None:
            text = text + f"{dummy_node.value} --->"
            dummy_node = dummy_node.next
        print(text)

    def count_elements(self):
        if self.head is None:
            print("Sorry the list is empty")
            return -1
        dummy_node = self.head
        counter = 0
        while dummy_node is not None:
            counter += 1
            dummy_node = dummy_node.next

        return counter

    def delete_at_index(self, index):
        if self.head is None:
            print("Sorry the list is empty")
            return -1

        elements = self.count_elements()

        if 0 > index or index >= elements:
            print("Sorry the index is out of range")
            return -1

        if index == 0:
            self.head = self.head.next
            return

        dummy_node = self.head
        counter = 0
        while counter + 1 != index:
            dummy_node = dummy_node.next
            counter += 1

        dummy_node.next = dummy_node.next.next
        if index == elements - 1:
            self.tail = dummy_node





