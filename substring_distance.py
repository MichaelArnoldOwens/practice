'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the size of the largest substring which starts and ends with the given *sub* string and return its length, including the length of the substrings. When *sub* is multiple characters, they may overlap with each other and share characters.

Example(s)
strDist("catcowcat", "cat") == 9
strDist("catcowcat", "cow") == 3
strDist("cccatcowcatxx", "cat") == 9
strDist("ooowhwhwooo", "whw") == 5


iter idx on string
    if idx = string.index(substring)
        do we set it as the start or end?
        start
            assume first instance is what we keep
        end
            assume last instance is what we keep


'''
def helper(string, i, substring, start = None, end = None):
    if i >= len(string):
        if end is None:
            return len(substring)
        return len(string[start:end]) + len(substring)
    sub = string[i:len(string)]
    if substring in sub and sub.index(substring) == 0:
        if start is None:
            start = i
        else:
            end = i
    return helper(string, i + 1, substring, start, end)

def strDist(arg, sub):
    return helper(arg, 0, sub)

print(strDist("catcowcat", "cat")) # 9
print(strDist("catcowcat", "cow") == 3)
print(strDist("cccatcowcatxx", "cat")) # 9
print(strDist("ooowhwhwooo", "whw") == 5)

