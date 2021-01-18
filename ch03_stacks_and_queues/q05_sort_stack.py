"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
"""

class Stack:
    def __init__(self):
        self._arr = []

    def is_empty(self):
        return not self._arr

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty")
        return self._arr[-1]

    def pop(self):
        result = self.peek()
        self._arr.pop()
        return result

    def push(self, value):
        self._arr.append(value)

    def sort_in_sec(self, sec):
        smallest = None
        count = 0
        while not self.is_empty():
            count += 1
            val = self.pop()
            if not smallest or smallest > val:
                smallest = val
            sec.push(val)

        removed = False
        while count > 0:
            count -= 1
            val = sec.pop()
            if not removed and val == smallest:
                removed = True
            else:
                self.push(val)

        sec.push(smallest)

    def sort_in_sec_v2(self, sec):
        if sec.is_empty():
            sec.push(self.pop())
            return

        val = self.pop()
        count = 0
        while not sec.is_empty():
            count += 1
            sec_val = sec.pop()
            self.push(sec_val)
            if sec_val <= val:
                break

        sec.push(val)
        while count > 0:
            count -= 1
            sec.push(self.pop())

    def sort(self):
        if self.is_empty():
            return

        sec = Stack()
        while not self.is_empty():
            self.sort_in_sec_v2(sec)

        while not sec.is_empty():
            self.push(sec.pop())

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack._arr)
    stack.sort()
    print(stack._arr)
