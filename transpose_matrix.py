'''
❓ PROMPT
In this task, we're going to apply basic 2-dimensional matrix traversals to solve some simple problems. While working on these, look out for other patterns you may have seen previously. Each of these takes the row- and column-major traversals and composites them with simpler ideas you have almost certainly encountered in one-dimensional array problems.

This task is two similar problems in one:
- First, write a function that returns the average of the smallest values in each _column_.
- Write a new version of this function that returns the average of the smallest value in each _row_.

For example, if the for the matrix:

[[1, 5, 3]
 [4, 2, 6]]

The smallest values in each column are 1, 2, and 3. The average of these is 2.

Remember that since we represent a matrix as nested arrays (an array of arrays), many problems on a matrix can be broken down into two array patterns. This makes them easier to reason about and code.

Example(s)
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
averageRowMinimum(matrix) == 4 (because average(5, 3) = 4)
'''
arr = [[1, 5, 3], [4, 2, 6]]

def avg_min_cols(arr):
    running_sum = 0
    for col in range(len(arr[0])):
        smallest_in_col = float('inf')
        for row in range(len(arr)):
            smallest_in_col = min(smallest_in_col, arr[row][col])
        running_sum += smallest_in_col
    avg = running_sum / len(arr[0])
    return avg

print(avg_min_cols(arr))
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
def averageRowMinimum(matrix):
    running_sum = 0
    for row in range(len(arr)):
        smallest_in_row = float('inf')
        for col in range(len(arr[0])):
            smallest_in_row = min(smallest_in_row, matrix[row][col])
        running_sum += smallest_in_row
    avg = running_sum / len(arr)
    return avg

print(averageRowMinimum(matrix))
