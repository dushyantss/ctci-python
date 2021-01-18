#! /usr/bin/python
"""
String Rotation:Assumeyou have a method isSubstring which checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
"""

def string_rotation(s1: str, s2: str):
    # We have to use is_substring
    # In the rotation, there will be two parts of the string which will switch places.
    # e.g. in waterbottle and erbottlewat; wat is first part and erbottle is the second part
    return len(s1) == len(s2) and is_substring(s1 + s1, s2) 

def is_substring(word: str, probable_substring: str):
    return probable_substring in word

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        str1, str2 = line.split(", ")
        str2 = str2[:-1] # This is done to remove the ending \n
        print(string_rotation(str1, str2))

