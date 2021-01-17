"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""

class Stack:
    def __init__(self, threshold):
        # Could optimize by creating internal array of threshold size but then popping and pushing become more complicated than required
        self._arr = []
        self._threshold = threshold

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
        if len(self._arr) < self._threshold:
            self._arr.append(value)
            return True
        return False
            

class SetOfStacks:
    def __init__(self, threshold):
        self._threshold = threshold
        self._arr = []
        self._arr.append(Stack(threshold))

    def is_empty(self):
        return self._arr[-1].is_empty()

    def peek(self):
        return self._arr[-1].peek()

    def pop(self):
        result = self._arr[-1].pop()
        if self._arr[-1].is_empty() and len(self._arr) > 1:
            # We remove stacks from the arr if they get empty. Except if it is the last stack, we will keep that to keep calculations easy
            self._arr.pop()
        return result

    def pop_at(self, i):
        # Not doing rollover as suggested in the solution as not specified.
        result = self._arr[i].pop()
        if self._arr[i].is_empty() and i != 0:
            self._arr.pop(i)
        return result

    def push(self, value):
        if not self._arr[-1].push(value):
            self._arr.append(Stack(self._threshold))
            self._arr[-1].push(value)


if __name__ == "__main__":
    stack = SetOfStacks(1)
    stack.push(1)
    stack.push(2)
    stack.push(0)
    stack.push(3)
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
    stack.pop()
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
    stack.pop()
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
    stack.pop()
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
    stack.pop()
    for a in stack._arr:
        print(a._arr)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop_at(1)
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
    stack.pop_at(0)
    print(stack.peek())
    for a in stack._arr:
        print(a._arr)
