'''
Go is an ancient game played on a board of 19x19 grid of lines. Black and white stones are placed at the intersections of these lines. A group of stones of one color is considered a _connected_ if every stone in the group is reachable from every other, traveling horizontally or vertically. For example, the following shows a is a single connected white group because we can traverse through all stones without jumps or moving diagonally.

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W W + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

A connected group of stones is captured when *all* adjacent points to the group are occupied by stones of the opposite color. Unoccupied intersections adjacent to a group of stones are called _liberties_. While playing the game, players must keep track of their groups and their liberty counts to look for strong moves to play.

The previous example group of white stones has 10 liberties. If the stone at (2, 3) is removed, it would be broken into two groups. The vertical group of three has 7 liberties, and the horizontal group of two has 6:

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W + + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

  0 1 2 3 4 5
0 W + + + + +
1 W B B B + +
2 + + B + + +
3 + + + + + +
4 + + + + + +
5 + + + + + +

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W + W +
3 + B W W W +7
4 + + + + + +
5 + + + + + +
'''

























#  // Interative DFS
#   def countLiberties(board, row, col):
#   color = board[row][col]
#   stack = [[row, col]]
#   liberties = 0
#   size = len(board)  # assuming square
#   checked = set()

#   def checkLocation(r, c):
#     key = f"{r},{c}"
#     if key in checked:
#       return
#     checked.add(key)

#     if r < 0 or r >= size:
#       return
#     if c < 0 or c >= size:
#       return
#     if board[r][c] == color:
#       stack.append([r, c])
#     if board[r][c] == '+':
#       nonlocal liberties
#       liberties += 1

#   while stack:
#     x, y = stack.pop()

#     checkLocation(x + 1, y)
#     checkLocation(x - 1, y)
#     checkLocation(x, y + 1)
#     checkLocation(x, y - 1)

#   return liberties



# # Recursive DFS
# def count_liberties(board, x, y):
#     visited = set()
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     liberties = 0

#     def dfs(r, c):
#         nonlocal liberties
#         if (r, c) in visited:
#             return
#         visited.add((r, c))

#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
