"""
Three in One: Describe how you could use a single array to implement three stacks.
"""

class Stack:
    def __init__(self, start, parent):
        self.start = start
        self.count = 0
        self.parent = parent

    def push(self, value):
        return self.parent.push(self, value)

    def pop(self):
        return self.parent.pop(self)

    def peek(self):
        return self.parent.peek(self)

    def is_empty(self):
        return self.parent.is_empty(self)

class MultiStack:
    CAPACITY = 10

    def __init__(self):
        self._arr = [None] * self.CAPACITY
        self.s1 = Stack(0, self)
        self.s2 = Stack(self.CAPACITY // 3, self)
        self.s3 = Stack(self.s2.start * 2, self)

    def stacks(self):
        return self.s1, self.s2, self.s3

    def is_empty(self, stack):
        return stack.count == 0

    def peek(self, stack):
        if self.is_empty(stack):
            raise Exception("Empty Stack")
        
        i = self.i_within(self.stack_i(stack) - 1)
        
        return self._arr[i]

    def pop(self, stack):
        result = self.peek(stack)
        stack.count -= 1
        i = self.stack_i(stack)
        self._arr[i] = None

        return result

    def i_within(self, i):
        return i % len(self._arr)

    def stack_i(self, stack):
        i = stack.start + stack.count
        return self.i_within(i)

    def collision(self, stack):
        i = self.stack_i(stack)
        if stack is self.s1 and i == self.s2.start:
                return self.s2
        elif stack is self.s2 and i == self.s3.start:
            return self.s3
        elif stack is self.s3 and i == self.s1.start:
            return self.s1

        return None

    def shift(self, collider):
        i = self.stack_i(collider)
        if i >= collider.start:
            # Simple case, in one line, so we shift each value ahead by one
            # We don't want to loop till collider.start as that one will be shifted by the value before it
            for j in range(i, collider.start, -1):
                self._arr[j] = self._arr[j - 1]
        else:
            # We need to loop twice and then also handle the middle value
            # First we move all the values from i to 0 one step forward
            # Then we copy the value in last index to 0
            # Then we move all the values from last index to start one step forward
            for j in range(i, 0, -1):
                self._arr[j] = self._arr[j - 1]

            self._arr[0] = self._arr[len(self._arr) - 1]

            for j in range(len(self._arr) - 1, collider.start, -1):
                self._arr[j] = self._arr[j - 1]

        collider.start += 1

    def adjust(self, collider):
        # There is space between the collider and its next value
        if not (second_collider := self.collision(collider)):
            self.shift(collider)
        # There is at least space between in the second collider and first collider
        # So, we shift both and create space
        elif not self.collision(second_collider):
            self.shift(second_collider)
            self.shift(collider)
        # No space in the entire array
        else:
            return False

        return True

    def push(self, stack, value):
        # Check if there is a collision
        if collider := self.collision(stack):
            # If collision, can we adjust
            # If we cannot adjust, raise error, else adjust
            if not self.adjust(collider):
                raise Exception("No space left in underlying array")
        
        # push the new value if no error raised
        i = self.stack_i(stack)
        self._arr[i] = value
        stack.count += 1

if __name__ == "__main__":
    multi = MultiStack()
    s1, s2, s3 = multi.stacks()

    s1.push(1)
    s2.push(1)
    s3.push(1)
    print(multi._arr)
    s1.push(2)
    s2.push(3)
    print(multi._arr)
    s1.push(3)
    print(multi._arr)
    s1.push(4)
    print(multi._arr)
    s1.push(5)
    print(multi._arr)
    s1.pop()
    print(multi._arr)
    s1.pop()
    print(multi._arr)
    s3.push(2)
    print(multi._arr)
    s3.push(3)
    print(multi._arr)
    s3.push(4)
    print(multi._arr)
    s2.pop()
    print(multi._arr)
    s2.push(2)
    print(multi._arr)
    s2.push(3)
    print(multi._arr)
    s1.push(6)

