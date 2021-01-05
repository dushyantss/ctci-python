#! /usr/bin/python
"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

from typing import List

# Manual test with matrix
# a b c
# d e f
# g h i
#
# expected
# g d a
# h e b
# i f c

# Test 2
# a b
# c d
#
# expected
# c a
# d b

# start with matrix as base input, start: 0, size: 3
def rotate_matrix(matrix: List[List[str]], start: int, end: int):
    # start: 0, end: 1
    # We go in layer by layer. First tackling the outer layers and then coming in
    
    # The bad+base case
    if start >= end:
        return matrix

    # First we tackle the top part and switch it with the right part
    # We don't want to loop till end as that is from the right part
    for i in range(start, end):
        # switch matrix[0][0] and matrix[0][2]
        # switch matrix[0][1] and matrix[1][2]
        
        # switch matrix[0][0] and matrix[0][1]
        matrix[start][i], matrix[i][end] = matrix[i][end], matrix[start][i]

    # current state
    # c f a
    # d e b
    # g h i

    # b a
    # c d
    
    # Then we do the same for the bottom part and the left part
    for i in range(end, start, -1):
        # switch matrix[2][2] and matrix[2][0]
        # switch matrix[2][1] and matrix[1][0]

        # switch matrix[1][1] and matrix[1][0]
        matrix[end][i], matrix[i][start] = matrix[i][start], matrix[end][i]

    # current state
    # c f a
    # h e b
    # i d g

    # b a
    # d c

    # Then we swap the new top and bottom parts in opposite order as they were not rotated
    for i in range(start, end):
        # switch matrix[0][0] and matrix[2][2]
        # switch matrix[0][1] and matrix[2][1]

        # switch matrix[0][0] and matrix[1][1]
        # From behind
        diff = i - start
        matrix[start][i], matrix[end][end - diff] = matrix[end][end - diff], matrix[start][i]

    # current state
    # g d a
    # h e b
    # i f c

    # c a
    # d b

    return rotate_matrix(matrix, start + 1, end - 1)

if __name__ == "__main__":
    import sys

    matrix = []
    for line in sys.stdin:
        pixels = line.replace("\n", "").split(", ")
        matrix.append(pixels)

    for row in matrix:
        print("".join(row))
    print("")
    rotated = rotate_matrix(matrix, 0, len(matrix) - 1)
    for row in rotated:
        print("".join(row))

