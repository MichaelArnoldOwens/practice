'''
❓ PROMPT
Given a target integer *X*, iterate from 1 to *X* and return a matrix sequence where each array starts with 1 and goes up to the current iteration. Each iteration should increment the array size and values until it reaches *X*.

[
[1],
[1, 2], 
[1, 2, 3],
[1, 2, 3, 4],
[1, 2, 3, 4, 5],
...
...
...
[1, 2, 3, ..., X]
]

Example(s)
generateSequence(2) == [[1], [1,2]]
generateSequence(3) == [[1], [1,2], [1,2,3]]
'''

def generateSequence(n):
    if n < 1:
        return []
    result = []
    for i in range(1, n + 1):
        sublist = []
        for num in range(1, i + 1):
            sublist.append(num)
        result.append(sublist)
    return result

genera

print(generateSequence(2))
print(generateSequence(3))
print(generateSequence(0) == [[]] or generateSequence(0) == [])
print(generateSequence(1) == [[1]])
print(generateSequence(2) == [[1], [1,2]])
print(generateSequence(3) == [[1], [1,2], [1,2,3]])
print(generateSequence(4) == [[1], [1,2], [1,2,3], [1,2,3,4]])

