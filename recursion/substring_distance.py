'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the size of the largest substring which starts and ends with the given *sub* string and return its length, including the length of the substrings. When *sub* is multiple characters, they may overlap with each other and share characters.

Example(s)
strDist("catcowcat", "cat") == 9
strDist("catcowcat", "cow") == 3
strDist("cccatcowcatxx", "cat") == 9
strDist("ooowhwhwooo", "whw") == 5
'''

def strDist(string, sub):
    if len(string) < len(sub):
        return 0
    if string.startswith(sub) and string.endswith(sub):
        return len(string)
    if not string.startswith(sub):
        return strDist(string[1:], sub)

    return strDist(string[:-1], sub)

print(strDist("catcowcat", "cat") == 9)
print(strDist("catcowcat", "cow") == 3)
print(strDist("cccatcowcatxx", "cat") == 9)
print(strDist("abccatcowcatcatxyz", "cat") == 12)
print(strDist("ooowhwhwooo", "whw") == 5)
print(strDist("xyx", "x") == 3)
print(strDist("xyx", "y") == 1)
print(strDist("xyx", "z") == 0)
print(strDist("z", "z") == 1)
print(strDist("x", "z") == 0)
print(strDist("", "z") == 0)
print(strDist("hiHellohihihi", "hi") == 13)
print(strDist("hiHellohihihi", "hih") == 5)
print(strDist("hiHellohihihi", "o") == 1)
print(strDist("hiHellohihihi", "ll") == 2)

