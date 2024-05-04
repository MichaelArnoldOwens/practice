'''
❓ PROMPT
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the usual 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

Example(s)
bunnyEarsTwist(2) == 5
bunnyEarsTwist(3) == 7
bunnyEarsTwist(5) == 12
''' 

def bunnyEarsTwist(n):
    if n == 1:
        return 2
    count = 3 if n % 2 == 0 else 2
    return count + bunnyEarsTwist(n-1)
print(bunnyEarsTwist(2))
print(bunnyEarsTwist(3) == 7)
print(bunnyEarsTwist(5) == 12)

