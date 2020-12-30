#! /usr/bin/python
"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith    ", 13 Output: "Mr%20John%20Smith"
"""

from typing import List

def urlify(arr: List[str], str_len: int):
    """
    Time: O(n)
    Space: O(1)
    """
    space_count = 0
    for i in range(str_len):
        if arr[i] == ' ':
            space_count += 1

    cur_last_index = (str_len - 1)
    new_last_index = cur_last_index + (space_count * 2)
    while cur_last_index != new_last_index: 
        if arr[cur_last_index] == ' ':
            arr[new_last_index - 2], arr[new_last_index - 1], arr[new_last_index] = '%', '2', '0'
            new_last_index -= 3
        else:
            arr[new_last_index] = arr[cur_last_index]
            new_last_index -= 1
        cur_last_index -= 1

    return arr

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        string, str_len = line.split(", ")
        str_len = int(str_len)
        url = urlify(list(string), str_len)
        assert len(url) == len(string)
        print("".join(url))

