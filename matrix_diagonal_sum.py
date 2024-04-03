"""
❓ PROMPT
Given a square matrix *mat*, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal *that are not part of the primary diagonal*.

Example(s)
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Element mat[1][1] = 5 is counted only once.

Input:
[[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]
Output: 8

Input: [[5]]
Output: 5
"""
def matrix_diagonal_sum(matrix):
    size = len(matrix)
    is_even = size % 2 == 0
    result = 0
    offset = 0
    for i in range(size):
        result += matrix[i][i]
    row = 0
    for i in range(size - 1, -1, -1):
        result += matrix[row][i]
        row += 1
    if not is_even:
        result -= matrix[size // 2][size // 2]
    return result

print(matrix_diagonal_sum([[1,2,3],
 [4,5,6],
 [7,8,9]]))
print(matrix_diagonal_sum([[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]))

