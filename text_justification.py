'''
Given an array of words and a max length per line, return an array of strings where each string represents a fully justified line. A fully justified line means that the first letter and last letter in the line should be a letter and not a space, and extra spaces are distributed as evenly as possible.

For the last line of text, it should be left-justified, and no extra space is inserted between words.
 

EXAMPLE(S)
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], k = 16

returns
["the  quick brown", // (2 spaces, 1 space)
"fox  jumps  over", // (2 spaces, 2 spaces)
"the lazy dog    "]  // (left justify, fill the end with 4 spaces)
 

FUNCTION SIGNATURE
function justify(words, maxWidth) { }
'''

def write_buffer(word_list, remaining_width):
    pass

def justify(words, maxWidth):
    result = []
    buffer = []
    capacity = maxWidth
    for word in words:
        if counter - len(word) < 0:
            result.append(write_buffer(buffer, capacity)
            capacity = maxWidth
            buffer = [word]
        


words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print(justify(words, k))



'''
def justify(words, maxWidth):
  counter = maxWidth
  result = []
  buffer = []

  for word in words:
    if counter - len(word) - len(buffer) < 0: # check this later
      result.append(build_string(buffer, counter))
      counter = maxWidth
      buffer = [word]
    else:
      counter -= len(word)
      buffer.append(word)
  # here we need to add the extra spaces to the last line
  # buffer = ["the", "lazy", "dog"]
  # last_line = "the lazy dog"
  last_line = " ".join(buffer) # js equivalent to Array.prototype.join(' ')
  remaining_spaces = maxWidth - len(last_line)
  last_line = f"{last_line}{' ' * remaining_spaces}"
  result.append(last_line)

def build_string(line, spaces_to_add): # list, number
  word_count = len(line)
  places_to_add_space_count = word_count - 1
  spaces_per_location = spaces_to_add // places_to_add_space_count
  locations_with_extra_space = spaces_to_add % places_to_add_space_count
  result = ''
  for i in range(0, len(line) - 1):
    word = line[i]
    if locations_with_extra_space > 0:
      result += word + (spaces_per_location + 1) * ' '
      locations_with_extra_space -= 1
    else:
      result += word + spaces_per_location * ' '
  result += line[-1]
  return result

  

print(build_string(["the", "quick", "brown"], 3))
'''
