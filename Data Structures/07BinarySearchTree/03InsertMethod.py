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

    # Itretively
    def insert_one(self, key):
        newNode = Node(key)
        if self.get_root() is None:
            self.root = newNode
            return
        root = self.get_root()
        while root:
            if root.key > key:
                if root.left is None:
                    root.left = newNode
                    break
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = newNode
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


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert_one(1)
    tree.insert_one(2)