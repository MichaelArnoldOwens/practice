def printSubSeq(string):
    x = 0
    def helper(string, seq=''):
        nonlocal x

        if not string:
            x+= 1
            if x == 5:
                print(seq)
            return
        helper(string[1:], seq+string[0])
        helper(string[1:], seq)
    helper(string)

printSubSeq('JOHN')


def printKSeq(seqLen, upperBound):
    res = []

    def helper(i, temp):
        if len(temp) == seqLen:
            res.append(temp.copy())
            return

        if i >= upperBound:
            return

        temp.append(i + 1)
        helper(i + 1, temp)
        temp.pop()
        helper(i + 1, temp)
        return

    helper(0, [])

    return res

printKSeq(seqLen=2, upperBound=3)

def permutations(arr):
    permutations = []
    x = 0

    def backtrack(start):
        nonlocal x
        x += 1

        if start == len(arr):
            permutations.append(arr[:])

        for i in reversed(range(start, len(arr))):
            arr[start], arr[i] = arr[i], arr[start]
            if x == 4: print(arr)
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    backtrack(0)

    return permutations

permutations(['A', 'B', 'C'])


def navigate(maze):
    x = 0

    def validMove(row, col):
        return 0 <= row < len(maze) \
        and 0 <= col < len(maze[0]) \
        and maze[row][col] != ' ' \
        and maze[row][col] != '*'

    def backtrack(row, col):
        nonlocal x
        x += 1
        if x == 9:
            print(maze[row][col])

        if maze[row][col] == '4':
            return

        maze[row][col] = '*'
        print(x)
        for r in maze:
            print(r)

        above = (-1, 0)
        right = (0, 1)
        below = (1, 0)
        left = (0, -1)
        clockwise = [above,right,below,left]

        for dr, dc in clockwise:
            newRow, newCol = row + dr, col + dc

            if validMove(newRow, newCol):
                backtrack(newRow, newCol)

    backtrack(0, 0)


maze =     [['5', ' ', ' ', 'A', ' '],
            ['B', 'C', 'D', 'E', ' '],
            [' ', ' ', 'F', ' ', '4'],
            ['G', 'H', 'I', ' ', 'J'],
            ['K', ' ', 'L', 'M', 'N']]

# navigate(maze)

def findWord(board, word):
    x = 0

    def validMove(row, col, idx):
        return 0 <= row < len(board) \
            and 0 <= col < len(board[0]) \
            and board[row][col] != '#' \
            and board[row][col] != '*' \
            and idx < len(word)

    def hasWord(row, col, idx):
        nonlocal x
        x += 1
        print(x)
        print('@:', row, col, idx)
        if x == 9:
            print("Visiting:", board[row][col])  # LOG LINE

        # Early-exit: if the letter at this word's index doesn't match
        # the current cell's letter, no reason to continue exploring
        if board[row][col] != word[idx]:
            return False
        # Base case: if we reach the last letter of the word and
        # the current cell's letter equals the last letter of the word
        elif idx == len(word) - 1 and board[row][col] == word[idx]:
            return True
        char = board[row][col]  # mark cell as visited
        board[row][col] = '#'

        for r in board:
            print(r)

        above = (-1, 0)
        below = (1, 0)
        left = (0, -1)
        right = (0, 1)
        clockwise = [left, below, right, above]  # counter-clockwise

        for dr, dc in clockwise:
            new_row, new_col = row + dr, col + dc
            if validMove(new_row, new_col, idx + 1):
                if hasWord(new_row, new_col, idx + 1):
                    return True
        board[row][col] = char  # undo

        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if hasWord(i, j, 0):
                return True

    return False


board = [
    ['D', 'P', 'D', 'A'],
    ['A', 'V', 'O', 'G'],
    ['T', 'O', 'N', 'Y'],
    ['J', 'E', 'S', 'S']
]

findWord(board, "DOG")