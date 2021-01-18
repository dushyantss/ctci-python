#! /usr/bin/python
"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

def palindrome_permutation(s: str):
    """
    Time: O(n)
    Space: O(n)
    """
    chars = {}
    for c in s:
        if c.isalpha():
            c = c.lower()
            chars[c] = chars.get(c, 0) + 1

    odd_chars_count = 0
    for v in chars.values():
        if v % 2 != 0:
            odd_chars_count += 1
            if odd_chars_count > 1:
                return False

    return True

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        print(palindrome_permutation(line))

