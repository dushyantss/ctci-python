"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

class Stack:
    def __init__(self):
        self._arr = []
        self._min_arr = []

    def is_empty(self):
        return not self._arr

    def peek(self):
        if not self._arr:
            raise Exception("Empty Stack")
        return self._arr[-1]

    def pop(self):
        result = self.peek()
        if self._min_arr[-1] == result:
            self._min_arr.pop()
        self._arr.pop()
        return result

    def push(self, value):
        if not self._min_arr or self._min_arr[-1] >= value:
            self._min_arr.append(value)
        self._arr.append(value)

    def min(self):
        if not self._min_arr:
            raise Exception("Empty Stack")
        return self._min_arr[-1]

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(0)
    stack.push(3)
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
