'''
❓ PROMPT
Define a subsequence of a string "s" to be a list of characters from "s" such that the characters appear in the same order in the list and in "s".

For instance, for the string "abcd", "a", "ab", and "acd" are valid subsequences, whereas "db" is not, since "b" comes before "d" in the original string.

Given an input string, return all subsequences except the empty string.

Example(s)
getAllSubsequences("abc") ==
  ["a", "b", "c", "ab", "ac", "bc", "abc"]
'''

# def getAllSubsequences(s):
#     subsequences = []
#     def helper(word, substr, i):
#         if i == len(word):
#             if len(substr) > 0:
#                 subsequences.append(substr)
#             return
#         helper(word, substr + word[i], i + 1)
#         helper(word, substr, i+1)
#     helper(s, '', 0)
#     return subsequences

def getAllSubsequences(word: str) -> list[str]:
  subsequences = []
  def getAllSubsequences(word, subseq, i):
    if i == len(word):
      if len(subseq) > 0:
        subsequences.append(subseq)
      return

    print('subseq with next letter:', subseq + word[i])
    print('subseq w/o next letter:', subseq)
    getAllSubsequences(word, subseq+word[i], i+1) # include the char
    print('##########calling second recursive call')
    getAllSubsequences(word, subseq, i+1) # omit the char

  getAllSubsequences(word, "", 0)
  return subsequences


# print(getAllSubsequences(('abc')))
# print(getAllSubsequences("abc") ==
#   ["a", "b", "c", "ab", "ac", "bc", "abc"])


# use a set for results to make them order agnostic
# print(getAllSubsequences("") == [])
# print(getAllSubsequences("a") == ["a"])
print(set(getAllSubsequences("ab")) == set(["b","a","ab"]))
# print(set(getAllSubsequences("abc")) == set(["c","b","bc","a","ac","ab","abc"]))
# print(set(getAllSubsequences("abcd")) == set(["d","c","cd","b","bd","bc","bcd","a","ad","ac","acd","ab","abd","abc","abcd"]))
# print(set(getAllSubsequences("1A")) == set(["A","1","1A"]))
# print(set(getAllSubsequences("1A2b")) == set(["b","2","2b","A","Ab","A2","A2b","1","1b","12","12b","1A","1Ab","1A2","1A2b"]))
# print(len(getAllSubsequences("jesitony")) == 255)