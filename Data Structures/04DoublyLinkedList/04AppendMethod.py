class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            print("Linked List is Empty")
            return True
        else:
            return False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def printList(self):
        if self.isEmpty():
            return
        current = self.head
        while current:
            print("Prev- {}\t Data - {}\t Next - {}".format(current.prev,
                                                            current.data, current.next))
            current = current.next
        return


if __name__ == "__main__":
    linkedList = DoublyLinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(4)
    linkedList.append(5)
    linkedList.printList()
