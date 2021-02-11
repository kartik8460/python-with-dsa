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

    def insert(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
            return
        current = self.root
        while current:
            if current.data > data:
                if current.left is None:
                    current.left = node
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                else:
                    current = current.right

    def delete(self, data):
        pass


if __name__ == "__main__":
    tree = BinarySearchTree()
