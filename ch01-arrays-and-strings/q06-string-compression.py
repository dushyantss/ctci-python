#! /usr/bin/python
"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def compress(text: str):
    if not text:
        return text

    prev = text[0] 
    count = 1
    result = []
    for _, c in enumerate(text, 1):
        if c != prev:
            result.append(prev)
            result.append(str(count))
            prev = c
            count = 1
        else:
            count += 1

    result.append(prev)
    result.append(str(count))

    new_text = "".join(result)
    if len(text) > len(new_text):
        return new_text
    else:
        return text

if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        # Remove newline character
        print(compress(line[:-1]))

