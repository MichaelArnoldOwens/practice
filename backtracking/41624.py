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

'''
❓ PROMPT
You are asked to write a program that simulates an ATM machine. The program should allow users to perform the following operations:

1. Check balance: Display the current balance of the user's account.
2. Deposit: Add money to the user's account.
3. Withdraw: Remove money from the user's account, if sufficient funds are available.

The program should have the following features:
- The program should be able to handle multiple user accounts.
- The program should store account balances persistently (i.e., in memory).
- The program should allow the user to specify the amount of money to deposit or withdraw.
- The program should validate user input and handle errors gracefully (e.g., invalid input, insufficient funds).
- The program should return appropriate messages to the user after each operation.

ATM Class Definition

- create_account(initial_balance) -> int: Creates a new account with an optional initial balance and returns the account ID.
- get_balance(account_id) -> float: Returns the balance of the account with the specified ID, or None if the account is not found.
- deposit(account_id, amount) -> str: Deposits the specified amount of money into the account with the specified ID and returns a string message describing the deposit. If the deposit is successful, the message should be in the following format: "Deposit successful: Your new balance is $<balance>.". If the deposit fails due to an error, the message should be in the following format:
"Deposit failed: Account not found."
- withdraw(account_id, amount) -> str: Withdraws the specified amount of money from the account with the specified ID and returns a string message describing the withdrawal. If the withdrawal is successful, the message should be in the following format: "Withdrawal successful: Your new balance is $<balance>.". If the withdrawal fails due to an error, the message should be in one of the following formats:
"Withdrawal failed: Account not found."
"Withdrawal failed: Insufficient funds."

Example(s)
atm = ATM()

# Create some accounts
account1 = atm.create_account()
account2 = atm.create_account(100.0)
account3 = atm.create_account(50.0)

# Deposit and withdraw money
print(atm.deposit(account1, 50.0))  # should print "Deposit successful: Your new balance is $50.00."
print(atm.withdraw(account1, 20.0))  # should print "Withdrawal successful: Your new balance is $30.00."
print(atm.withdraw(account1, 40.0))  # should print "Withdrawal failed: Insufficient funds."
'''

class ATM:
    def __init__(self):
        pass

    def create_account(self, initial_balance):
        pass

    def get_balance(self):
        pass

    def deposit(self, account_id, amount):
        pass

    def withdraw(self, account_id, amount):
        pass



