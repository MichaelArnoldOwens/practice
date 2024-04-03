"""
❓ PROMPT
This exercise is great for building a solid understanding of working with complex data structures.

Write functions that take a multidimensional array as input and then output a single dimensional array. Start with the elements in increasing _row major_ order, meaning the first row from beginning to end, then the second row, etc. Then move on to _column major_, which is the first column from beginning to end and then the second, etc.

You can use this template to get started:

function template(matrix) {
  const result = [];

  // Your code here.

  return result;
}

As a final challenge, do additional versions where each row is output backward but the rows are in order and similarly for columns. There are actually 4 different variations for both row and column major, so 8 total. Do you see why?

As you work through the variations, take note of what changes are required between variations:
- What changes between forward and backward along any dimension?
- What is the pattern in the code that differentiates row major vs column major?

*Python Programmers*: Be sure to do at least one of these variations using both manual counting loops (incrementing an index variable) and also using the range() construct. The range() function is great when you already understand this thoroughly but writing some manual loops will help you build that understanding.

Example(s)
let matrix = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]
];
"""

matrix = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]
]

def row_traversal(arr):
    result = []
    for row in arr:
        for col in row:
            result.append(col)
    return result

def row_traversal_range(arr):
    result = []
    for row_index in range(len(arr)):
        row = arr[row_index]
        for col_index in range(len(row)):
            result.append(row[col_index])
    return result

# print(row_traversal((matrix)))
# print(row_traversal_range(matrix))

def col_traversal(arr):
    result = []
    for col in range(len(arr[0])):
        for row in range(len(arr)):
            result.append(arr[row][col])

    return result
# print(col_traversal((matrix)))

def row_reverse(arr):
    result = []
    for row_index in range(len(arr)):
        for col_index in range(len(arr[row_index]) - 1, -1, -1):
            result.append(arr[row_index][col_index])
    return result
# print(row_reverse(matrix))

def col_reverse(arr):
    result = []
    for col_index in range(len(arr[0])):
        for row_index in range(len(arr) - 1, -1, -1):
            result.append(arr[row_index][col_index])
    return result
print(col_reverse(matrix))
