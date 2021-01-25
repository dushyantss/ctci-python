"""
Number Swapper: Write a function to swap a number in place (that is, without temporary variables).
"""

def number_swapper(a, b):
    b = a ^ b
    a = b ^ a
    b = b ^ a
    return a, b

if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        a, b = line.strip().split()
        a, b = int(a), int(b)
        print(number_swapper(a, b))

