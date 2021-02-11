class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    # Itretively
    def insert_one(self, key):
        new_node = Node(key)
        if self.get_root() is None:
            self.root = new_node
            return
        root = self.get_root()
        while root:
            if root.key > key:
                if root.left is None:
                    root.left = new_node
                    break
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = new_node
                    return
                else:
                    root = root.right

    # Recursively
    def insert_two(self, key):
        if self.is_empty():
            self.root = Node(key)
            return

        def insert_helper(current, key):
            if current.key > key:
                if current.left is None:
                    current.left = Node(key)
                else:
                    insert_helper(current.left, key)
            else:
                if current.right is None:
                    current.right = Node(key)
                else:
                    insert_helper(current.right, key)

        insert_helper(self.get_root(), key)

    def delete(self, key):
        if self.is_empty():
            pass


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert_one(1)
    tree.insert_one(2)