'''
❓ PROMPT
Given a string, recursively compute a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a"
'''

def pairStars(input, result=''):
    if len(input) == 0:
        return result
    newStr = result
    if len(result) > 0:
        if input[0] == result[-1]:
            return pairStars(input[1:], result + '*' + input[0])
        else:
           return pairStars(input[1:], result + input[0])
    else:
        return pairStars(input[1:], result + input[0])


print( pairStars("hello") == "hel*lo" )
print( pairStars("xxyy") == "x*xy*y" )
print( pairStars("aaaa") == "a*a*a*a" )

