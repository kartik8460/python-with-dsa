class Node:
    def __init(self, key):
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

    def print_tree(self):
        if self.is_empty():
            print("Tree is Empty")
            return
        root = self.get_root()


if __name__ == "__main__":
    tree = BinarySearchTree()
