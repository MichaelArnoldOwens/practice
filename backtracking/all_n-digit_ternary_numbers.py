'''
❓ PROMPT
The decimal system uses the digits 0-9, the binary system uses the digits 0 and 1, and the hexadecimal system uses the digits 0-9 and the letters A-F.  The ternary system is a base-3 numeral system that uses the digits 0, 1, and 2.

Given a number *n*, write a function that generates all *n*-digit ternary numbers.

Example(s)
Numbers starting with zero shouldn't normally be included but the ternary representing the zero value is a valid 1-digit ternary. No other strings should start with a "0"!

generateNDigitTernaries(1) == ["0","1","2"]
generateNDigitTernaries(2) == ["10","11","12","20","21","22"]

Ideas:
so for each ternary that has > 1 digit:
  we can pick 1 from 3 possible numbers {0, 1, 2}
  


'''

def generateNDigitTernaries(n):
  result = []
  def helper(subset, i):
    if i == n:
      result.append(subset)
      return

    for j in '012':
      if j == '0' and i == 0:
        continue
      helper(subset + j, i + 1)

  helper('', 0)

  return result

print(generateNDigitTernaries(1))

print(generateNDigitTernaries(2))

