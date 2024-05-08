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

