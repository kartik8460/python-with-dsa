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

    def push(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = self.head

        if temp is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
        else:
            newNode.next = newNode
        self.head = newNode

    def printList(self):
        if self.isEmpty():
            return
        current = self.head
        while True:
            print(current.data)
            if(current.next == self.head):
                break
            current = current.next


if __name__ == "__main__":
    linkedList = CircularLinkedList()
    linkedList.push(5)
    linkedList.push(4)
    linkedList.push(3)
    linkedList.push(2)
    linkedList.push(1)
    linkedList.printList()
