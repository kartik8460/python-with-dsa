class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
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
        temp = self.head
        while(temp.next != self.head):
            print(temp.data)


if __name__ == "__main__":
    linkedList = CircularLinkedList()
    linkedList.printList()
