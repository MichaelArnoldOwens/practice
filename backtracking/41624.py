'''
The programming interface for a legacy motor controller accepts commands as binary strings of variable length. The console has a very primitive autocomplete autocorrect feature: given an incomplete command, it will display possible commands that has the incomplete command as a prefix. For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result.

Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.


EXAMPLE(S)
Possible commands = ['000', '1110', '01', '001', '110', '11']

'0' → ['000', '01', '001']
'1' → ['1110', '110', '11']
'00' → ['000', '001']


FUNCTION SIGNATURE
Implement a class that should be initialized with a list of possible commands. The class should have the following public method:

autocomplete(command) {
def autocomplete(self, command: str) -> list[str]:

class Search()

def __init__(listOfPossibleWords)

def autocomplete(self, command: str) -> list[str]:

search = Search(listOfPossibleWords)
search.autocomplete("0") -> ['000', '01', '001']
search.autocomplete("2") -> []

TRIE

'''
'''
EXPLORE 

BRAINSTORM

[Aba, Aca, Ada, Aea, Afa]

[aba]


PLAN


class TrieNode ()

  def __init__(self, isComplete \\ false , value \\ null):
    self.isComplete = isComplete
    self.value = value
    self.children = {
      // value: TrieNode
    }


class Search

  def __init__(self, listOfPossibleWords):
    self.trie = new Trie()

    iterate over listOfPossibleWords
      for each word, start from parent trie
        currTrie = self.trie
        for each character 
          if currTrie does not have the character
            create new TrieNode
            currTrie.children.set(trieNode.value, trieNode)
            currTrie = the new trie node
          else 
            currTrie = currTrie.children.get(character)

        currTrie.isComplete = true;

  def autocomplete(self, command: str) -> list[str]:
    # my impl
    idx = 0
    curr_char = command[idx]
    result = []
    def helper(commandSoFar, node, idx):
      if idx >= len(command) - 1 and node.isComplete:
        result.append(commandSoFar)

      targetLetter = command[idx]
      if targetLetter in node.children:
        helper(commandSoFar + targetLetter, node.children[targetLetter], idx + 1)
      # instructor's impl  
      let currNode = self.trie

      for index in len(command):
        if command[index] in currNode.children:
          currNode = currNode.children[command[index]]
        else:
          return []

      currNode
      let result = []

      def helper(currNode, prefix)
        if currNode.isComplete:
          result.append(prefix+currNode.value)
        for children in currNode.children:
          helper(children, prefix+currNode.value)

      helper(currNode)
      return result


    helper('', self.trie, idx)
    return result


'''
