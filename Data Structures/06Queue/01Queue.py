class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def getSize(self):
        return len(self.data)

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        pop = self.data.pop(0)
        return pop

    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        for i in self.data:
            print(i)


if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    print(queue.getSize())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.isEmpty())
    print(queue.getSize())
    queue.printQueue()
    print("Dequeue Element is :", queue.dequeue())
    queue.printQueue()
    print(queue.getSize())
