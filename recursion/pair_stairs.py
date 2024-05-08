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

# def pairStars(word, index=0):
#     if index == len(word):
#         return ''
#     substring = pairStars(word, index + 1)

#     if len(substring) > 0 and word[index] == substring[0]:
#         return word[index] + '*' + substring

#     return word[index] + substring


def pairStars(word: str, index=0) -> str:
  if len(word) <= 1:
    return word

  if index == len(word)-1:
    return word[index]

  if word[index] == word[index+1]:
    return word[index] + "*" + pairStars(word, index + 1)

  return word[index] + pairStars(word, index + 1)



print( pairStars("hello") == "hel*lo" )
print( pairStars("xxyy") == "x*xy*y" )
print( pairStars("aaaa") == "a*a*a*a" )

