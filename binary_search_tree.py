class BinarySearchTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, data) -> None:
        """
        Adds new Node with value to the tree
        """

        if not self.value:
            self.value = data
            return

        if data == self.value:
            return

        if data < self.value:
            if self.left:
                self.left.add_node(data)
                return
            self.left = BinarySearchTreeNode(value=data)
            return

        if data > self.value:
            if self.right:
                self.right.add_node(data)
                return
            self.right = BinarySearchTreeNode(value=data)
            return

    def search(self, value) -> bool:
        """
        Checks if the given value is already in the tree
        """
        if self.value is None:
            return False

        if self.value == value:
            return True

        if value < self.value:
            if self.left:
                return self.left.search(value)
            return False

        if value > self.value:
            if self.right:
                return self.right.search(value)
            return False

        return False

    def get_max(self):
        """Gets the biggest value of the tree"""
        if self.value is None:
            return

        if self.right:
            return self.right.get_max()

        return self.value

    def get_min(self):
        """Gets the smallest value of the tree"""
        if self.value is None:
            return

        if self.left:
            return self.left.get_min()

        return self.value

    def in_order_traversal(self, traversal_list=[]):
        """First traverses the left subtree, then the root and at last the right subtree."""
        if self.value is None:
            return []

        if self.left:
            self.left.in_order_traversal(traversal_list)

        traversal_list.append(self.value)

        if self.right:
            self.right.in_order_traversal(traversal_list)

        return traversal_list

    def pre_order_traversal(self, traversal_list=[]):
        """First traverses the root, then the left subtree and at last the right subtree."""
        if self.value is None:
            return []

        traversal_list.append(self.value)

        if self.left:
            self.left.pre_order_traversal(traversal_list)

        if self.right:
            self.right.pre_order_traversal(traversal_list)

        return traversal_list

    def post_order_traversal(self, traversal_list=[]):
        """First traverses the left subtree, then the right subtree and at last the root."""
        if self.value is None:
            return []

        if self.left:
            self.left.post_order_traversal(traversal_list)

        if self.right:
            self.right.post_order_traversal(traversal_list)

        traversal_list.append(self.value)

        return traversal_list

    def delete_value(self, value):
        if self.value is None:
            return

        elif value < self.value:
            if self.left:
                self.left = self.left.delete_value(value)

        elif value > self.value:
            if self.right:
                self.right = self.right.delete_value(value)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                right_subtree_min_value = self.right.get_min()
                self.value = right_subtree_min_value
                self.right = self.right.delete_value(right_subtree_min_value)

        return self


