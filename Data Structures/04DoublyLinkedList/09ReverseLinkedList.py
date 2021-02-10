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
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode
            newNode.prev = last

    def insertAt(self, data, prevData):
        if self.isEmpty():
            return
        if prevData is None:
            print("Previous Data cannot be null")
        newNode = Node(data)
        previous = self.head
        while previous:
            if previous.data == prevData:
                break
            previous = previous.next
        if previous is not None:
            newNode.next = previous.next
            newNode.prev = previous
            previous.next = newNode
            if newNode.next is not None:
                newNode.next.prev = newNode

        else:
            print("Element Not Found")

    def delete(self, data):
        if self.isEmpty():
            return
        if data == self.head.data:
            current = self.head
            self.head = current.next
            self.head.prev = None
            del current.data
            current.next = None
            return

        node = self.head
        while node:
            if node.data == data:
                break
            node = node.next
        if node is None:
            print("Element Not Found")
            return
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        del node.data
        node.next = None
        node.prev = None

    def deleteList(self):
        if self.isEmpty():
            return
        current = self.head
        next = None
        while current:
            next = current.next
            del current.data
            current.next = None
            current.prev = None
            current = next
        self.head = None

    def reverseList(self):
        if self.isEmpty():
            return
        current = self.head
        next = None
        prev = None

        while current:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        self.head = prev

    def count(self):
        if self.isEmpty():
            return
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print("Count is :", count)

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
    print("**********Before Reversing**********")
    linkedList.printList()
    print("**********After Reversing***********")
    linkedList.reverseList()
    linkedList.printList()
