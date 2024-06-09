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
'''
class ATM:
  def __init__(self):
    self.accounts = {}
    self.next_new_account_id = 1

  def create_account(self, initial_amt = 0):
    if initial_amt < 0:
      print('Invalid initial amount')
      return
    account_id = str(self.next_new_account_id)
    self.accounts[account_id] = initial_amt
    self.next_new_account_id += 1
    return account_id

  def deposit(self, acc, amt):
    if acc not in self.accounts:
      return f'Account {acc} does not exist'

    self.accounts[acc] += amt
    return f'Deposit successful: Your new balance is ${self.accounts[acc]:.2f}.'
  

  def withdraw(self, acc, amt):
    if amt > self.accounts[acc]:
      return print('Withdrawal failed: Insufficient funds.')
    
    self.accounts[acc] -= amt
    return f'Withdrawal successful: Your ne wbalance is ${self.accounts[acc]:.2f}.'


atm = ATM()

# Create some accounts
account1 = atm.create_account()
account2 = atm.create_account(100.0)
account3 = atm.create_account(50.0)

# Deposit and withdraw money
print(atm.deposit(account1, 50.0))  # should print "Deposit successful: Your new balance is $50.00."
print(atm.withdraw(account1, 20.0))  # should print "Withdrawal successful: Your new balance is $30.00."
print(atm.withdraw(account1, 40.0))  # should print "Withdrawal failed: Insufficient funds."
 
