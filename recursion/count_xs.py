'''
❓ PROMPT
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0
'''
def countX(input, current = 0):
    if len(input) == 0:
        return current
    if input[0] == 'x':
        return countX(input[1:], current + 1)
    else:
        return countX(input[1:], current)
    

print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hi") == 0)

