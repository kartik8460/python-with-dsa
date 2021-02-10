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
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(5)
    print("**********Before Inserting**********")
    linkedList.printList()
    print("**********After Inserting**********")
    linkedList.insertAt(4, 5)
    linkedList.printList()
