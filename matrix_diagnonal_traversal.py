'''
❓ PROMPT
Write a function that traverses a matrix in diagonal fashion, starting from the bottom left corner. For example if the input matrix is:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

Then the desired output is:

[7, 4, 8, 1, 5, 9, 2, 6, 3]

Example(s)
[
  [1, 2],
  [3, 4],
] -> [3, 1, 4, 2]


condition = row >= 0
last_row = len(m) - 1
first_col = 0

last_row - 1
  for i range(0, first_col + 2)
    print(m[last_row - 1][i])
    last_row + 1

last_row - 2

''' 

# def traverse_matrix_diagonal(m):
#   if len(m) == 1:
#     return m[0]
#   result = []
#   start_row_idx = len(m) - 1
#   end_col_idx = 1
#   while start_row_idx >= 0:
#     for i in range(0, end_col_idx):
#       result.append(m[start_row_idx + i][i])
# 
#     start_row_idx -= 1
#     end_col_idx += 1
# 
#   start_col_idx = 1
#   end_row_idx = 2 
# 
#   while start_col_idx < len(m[0]):
#     for i in range(0, end_row_idx):
#       result.append(m[i][start_col_idx])
#       start_col_idx += 1
#       end_row_idx += 1
# 
#   result.append(m[len(m) - 1][len(m[0]) - 1 ])
# 
#   return result
def diagonal_traversal(m):
    if len(m) == 0 or len(m[0]) == 0:
        return []
    
    nr = len(m) # number of rows
    nc = len(m[0]) # number of columns

    starts = []
    for i in range(nr - 1, 0, -1):
        starts.append([i, 0])
    for i in range(nc):
      starts.append([0, i])

    output = []
    for sr, sc in starts:
      i = 0
      while sr + i < nr and sc + i < nc:
        output.append(m[sr+ i][sc + i])
        i += 1

    return output
      


matrix =  [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

print(diagonal_traversal(matrix))

print(diagonal_traversal([[1]]))
print(diagonal_traversal([[1],[2]]))
