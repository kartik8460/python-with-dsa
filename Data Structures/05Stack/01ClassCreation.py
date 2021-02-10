class Stack:
    def __init__(self, limit):
        self.top = None
        self.data = []
        self.limit = limit

    def getSize(self):
        return len(self.data)

    def getLimit(self):
        return self.limit

    def isFull(self):
        if self.getSize() == self.limit:
            return True
        else:
            return False

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Cannot perform push() as Stack is Full")
            return

        self.data.append(data)
        self.top = data

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.top

    def pop(self):
        if self.isEmpty():
            print("Cannot perform pop() as Stack is Empty")
            return
        pop = self.data.pop()
        if self.isEmpty():
            self.top = None
        else:
            self.top = self.data[self.getSize()-1]
        print("Poped Element ", pop)
        return pop

    def printStack(self):
        print()
        print("********** Stack Below **********")
        for i in range(self.getSize()-1, -1, -1):
            print("\t|\t{}\t|".format(self.data[i]))
            print("\t-----------------")
        print("********** Stack   End **********")
        print()


if __name__ == "__main__":
    stack = Stack(5)
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.push(5)
    stack.printStack()
    print("Size of the Stack is", stack.getSize())
    print("Peek of the Stack is", stack.peek())
    print("Limit of the Stack is", stack.getLimit())
    stack.push(6)
