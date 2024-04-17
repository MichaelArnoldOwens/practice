'''
In most spreadsheets, the rows are named with numbers (starting at 1), and the columns are given names that are strings of capital letters. The first column is 'A', the second is 'B' up to the 26th which is 'Z'. At that point, they progress to 'AA' for 27, then 'AB' for 28, etc.

As part of our new product, we need functions to convert between these column header strings and their ordinal values, and vice versa!

Start out with the column-header-to-ordinal direction. If you get that working, do the inverse!

The challenges arise from our labeling system not having a character that represents zero. This problem will make you thankful that ancient Babylonian, Chinese, and other civilizations came up with the idea of zero.


EXAMPLE(S)
columnToOrdinal("A") => 1
columnToOrdinal("J") => 10
columnToOrdinal("Z") => 26
columnToOrdinal('AA') => 27
columnToOrdinal('AB') => 28 => 26 +1
columnToOrdinal('AZ'), 52);
columnToOrdinal('BA'), 53); 26^1 * 'B' + 26^0 * 'A'
columnToOrdinal('JJ'), ); 26^1 * 'J' + 26^0 * 'J'
columnToOrdinal('ZZ'), 702); 26*27 (26 + 26x26) => A-Z + A(a-Z), B(a-Z), ... Z(A-Z)
columnToOrdinal('AAA'), 703); 26^2 (676) + 26^1 (26) + 26^0 (1) = 703


columnToOrdinal('CBA'), ) -> 26^2 * 'C' + 26^1 * 'B' + 26^0 * 'A'

- J -> ascii('J') - ascii('A')  => nth position


- A -> ascii('A') - ascii('A') + 1
- C -> ascii(C) - ascii(A) + 1 = 3


- for loop going through letters:
  - get the power value associated with the letter
  - get the ASCII value associated with the letter
  - do the math! 26^power * letter value
  - add to sum

return sum

- one letter: 1-26
- two letters: 26 - 26^2
- 3 letters: 26^2 - 26^3



ordinalToColumn(1) => "A"
ordinalToColumn(26) => "Z"
ordinalToColumn(27) => "AA"
ordinalToColumn(52) => "AZ"


680 / 26 = 26 (Z)
680 % 26 = 4 (D)

680 -> ZD


703 - AAA

703 / 26 = 27
703 % 26 = 1 (A)

27 / 26 = 1 (A)
27 % 1 = 1 (A)

AAA

list = []

while sum > 0:
  sum % 26 = rem
  the letter associated with the remainder
  add letter to list

  sum = sum / 26
  if sum > 26:
    continue

return the list (reversed)



function ordinalToColumn(ord) {
  const reversed = [];
  while (ord > 0) {
    ord--;
    reversed.push(String.fromCharCode('A'.charCodeAt() + (ord%26)));
    ord = Math.floor(ord / 26);
  }

  return reversed.reverse().join('');
}




'''

# def columnToOrdinal(headerStr):
#   sum = 0
#   for idx in range(len(headerStr)):
#     curr_char = headerStr[idx]
#     sum *= 26
#     sum +=  (ord(curr_char) - ord('A') + 1)
#   return sum

def columnToOrdinal(headerStr):
  sum = 0
  exponent = len(headerStr) - 1
  for idx in range(len(headerStr)):
    curr_char = headerStr[idx]
    sum += 26**exponent * (ord(curr_char) - ord('A') + 1)
    exponent -= 1
  return sum

print(columnToOrdinal('A'))
print(columnToOrdinal('AA'))
print(columnToOrdinal('AAA'))


def ordinalToColumn(ordinal):
  pass