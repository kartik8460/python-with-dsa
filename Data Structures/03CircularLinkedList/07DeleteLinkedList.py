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

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = newNode
            newNode.next = self.head

    def insertAt(self, data, prevData):
        if self.isEmpty():
            return
        newNode = Node(data)
        current = self.head
        while current:
            if current.data == prevData:
                newNode.next = current.next
                current.next = newNode
                return
            if current.next == self.head:
                break
            current = current.next
        print("Element Not Found")

    def delete(self, data):
        if self.isEmpty():
            return
        if self.head.data == data and self.head.next == self.head:
            del self.head.data
            self.head = None
            return
        elif self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            current = None
            return
        else:
            current = self.head
            prev = None
            while True:
                prev = current
                current = current.next
                if current.data == data:
                    break
                if current == self.head:
                    print("Element Not Found")
                    return

            prev.next = current.next
            current = None

    def deleteList(self):
        if self.isEmpty():
            return

        current = self.head
        while current:
            next = current.next
            del current.data
            current.next = None
            current = next
            if current == self.head:
                break
        self.head = None

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
    print("**********Before Deletion**********")
    linkedList.printList()
    print("**********After Deletion***********")
    linkedList.deleteList()
    linkedList.printList()
