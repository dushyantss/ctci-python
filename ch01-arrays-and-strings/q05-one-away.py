#! /usr/bin/python
"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false
"""

def one_away(s1: str, s2: str):
    # If the diff in len is > 1, they'll need more than 1 edit to become the same.
    if abs(len(s1) - len(s2)) > 1:
        return False

    # if diff is 0, only one replacement is allowed.
    if len(s1) == len(s2):
        replacements = 0
        for i, c in enumerate(s1):
            if c != s2[i]:
                replacements += 1
            if replacements > 1:
                return False
        return True

    # if diff is 1, either one insertion or one removal, both will work the same.
    # So, we'll just count the skips required and if there are more than one, we return False;

    # We consider s1 to be the longer string, always
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    # There are two places where can get error, if sw[i - skips] fails happens at the first i or the last i.
    # So, either s2[0] is invalid or the difference is on the last character.
    skips = 0
    for i, c in enumerate(s1):
        skipped_i = i - skips
        if skipped_i < 0 or skipped_i >= len(s2):
            return True;
        if c != s2[skipped_i]:
            skips += 1
        if skips > 1:
            return False

    return True

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        str1, str2 = line.split(", ")
        # This is done to remove the newline
        str2 = str2[:-1]
        print(one_away(str1, str2))

