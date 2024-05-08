'''
❓ PROMPT
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. Use recursion to solve this problem (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while integer division by 10 removes the rightmost digit (126 / 10 is 12). Be aware that some languages require some special handling to do integer division while others do not.
'''

def count7(num):
    if num == 0:
        return 0
    
    if num % 10 == 7:
        return 1 + count7(num // 10)
    return count7(num // 10)

print(count7(7))
print(count7(123))
print(count7(717))
