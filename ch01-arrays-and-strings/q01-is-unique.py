#! /usr/bin/python
"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

def is_unique(s: str):
    return is_unique_no_additional_ds(s)

def is_unique_no_additional_ds(s: str):
    """
    Since we cannot modify a string, I've had to create a list from the string.
    If we are provided a mutable string, we could sort in place.
    Time: O(n log(n)), Space: O(1)
    """
    l = list(sorted(s))
    for i, c in enumerate(l):
        if i < len(l) - 2:
            if c == l[i + 1]:
                return False

    return True

def is_unique_with_set(s: str):
    """
    Time: O(n), Space: O(n)
    """
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)

    return True

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        print(is_unique(line))

