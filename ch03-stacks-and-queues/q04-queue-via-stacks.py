"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:
    def __init__(self):
        # s1 will contain the properly ordered queue, s2 is the supporting stack
        self.s1, self.s2 = [], []

    def shift(self):
        if not self.s1:
            for _i in range(len(self.s2)):
                self.s1.append(self.s2.pop())

    def is_empty(self):
        self.shift()
        return not self.s1

    def peek(self):
        self.shift()
        if self.is_empty():
            raise Exception("Empty Queue")
        return self.s1[-1]

    def remove(self):
        self.shift()
        result = self.peek()
        self.s1.pop()
        return result

    def add(self, value):
        self.s2.append(value)

if __name__ == "__main__":
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    print(queue.s1)
    print(queue.peek())
    print(queue.remove())
    print(queue.s1)
