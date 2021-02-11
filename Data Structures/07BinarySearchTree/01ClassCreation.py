class Node:
    def __init__(self, data):
        self.data = data
        self.left = 0
        self.right = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False


if __name__ == "__main__":
    tree = BinarySearchTree()
