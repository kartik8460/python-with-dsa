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
    linkedList.printList()
