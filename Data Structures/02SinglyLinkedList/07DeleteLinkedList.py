class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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
        self.head = newNode

    def append(self, data):
        if self.isEmpty():
            self.push(data)
            return

        newNode = Node(data)
        current = self.head

        while(current.next):
            current = current.next
        current.next = newNode

    def insertAt(self, data, prevData):
        if self.isEmpty():
            return

        newNode = Node(data)
        prevNode = self.head
        while(prevNode):
            if prevData == prevNode.data:
                break
            prevNode = prevNode.next

        if prevNode is None:
            print("Cannot Find Previous Node")
            return

        newNode.next = prevNode.next
        prevNode.next = newNode

    def delete(self, data):
        if self.isEmpty():
            return

        if self.head.data == data:
            del self.head.data
            self.head = self.head.next
            return

        prevNode = None
        currentNode = self.head
        while(currentNode and currentNode.data != data):
            prevNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            print("Element Does not Exist")
            return
        prevNode.next = currentNode.next
        del currentNode.data
        currentNode = None

    def deleteList(self):
        if self.isEmpty():
            return
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
        self.head = None

    def printList(self):
        if self.isEmpty():
            return
        current = self.head
        while(current):
            print(current.data)
            current = current.next


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    linkedList.push(2)
    linkedList.push(1)
    linkedList.append(3)
    linkedList.append(4)
    linkedList.insertAt(5, 4)
    print("**********Before Deleting the Linked List**********")
    linkedList.printList()
    print("**********After Deleting the Linked List**********")
    linkedList.deleteList()
    linkedList.printList()
