'''
❓ PROMPT
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

Example(s)
changePi("xpix") == "x3.14x"
changePi("pipi") == "3.143.14"
changePi("pip") == "3.14p"
'''
def changePi(input):
    if len(input) <= 1:
        return input
    if input[0:2] == 'pi':
        return '3.14' + changePi(input[2:])
    return str( input[0] ) + changePi(input[1:])


print(changePi("xpix") == "x3.14x")
print(changePi("pipi") == "3.143.14")
print(changePi("pip") == "3.14p")



