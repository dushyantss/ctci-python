#! /usr/bin/python
"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(s1: str, s2: str):
    """
    Here we have used a dict to store all the chars in s1 and compare them with s2.
    Time: O(n), Space: O(n)
    
    If we want a 0 extra space algorithm, we could sort the two strings in place and go char by char and check.
    Time: O(n log(n)), space: O(1)
    """
    s1_chars = {}
    for c in s1:
        s1_chars[c] = s1_chars.get(c, 0) + 1

    for c in s2:
        if s1_chars.get(c, 0) == 0:
            return False
        else:
            s1_chars[c] -= 1

    return True

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        str1, str2 = line.split()
        print(check_permutation(str1, str2))

