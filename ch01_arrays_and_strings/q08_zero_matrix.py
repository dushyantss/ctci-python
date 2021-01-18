#! /usr/bin/python
"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

from typing import List

# 1 2 0
# 3 4 5

# 0 0 0
# 3 4 0
def zero_matrix(matrix: List[List[int]]):
    if not matrix or not matrix[0]:
        return matrix

    row_has_zero, col_has_zero = 0, 0
    row_len, col_len = len(matrix), len(matrix[0])

    for i in range(col_len):
        if matrix[0][i] == 0:
            row_has_zero = True
            break

    for i in range(row_len):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    for i in range(1, row_len):
        for j in range(1, col_len):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(col_len):
        if matrix[0][i] == 0:
            for j in range(1, row_len):
                matrix[j][i] = 0

    for i in range(row_len):
        if matrix[i][0] == 0:
            for j in range(1, col_len):
                matrix[i][j] = 0

    if row_has_zero:
        for j in range(col_len):
            matrix[0][j] = 0

    if col_has_zero:
        for i in range(row_len):
            matrix[i][0] = 0

    return matrix

if __name__ == "__main__":
    import sys

    matrix = []
    for line in sys.stdin:
        words = line.replace("\n", "").split(", ")
        ints = [int(c) for c in words]
        matrix.append(ints)

    for row in matrix:
        print("".join((str(c) for c in row)))
    print("")
    zeroed = zero_matrix(matrix)
    for row in zeroed:
        print("".join((str(c) for c in row)))

