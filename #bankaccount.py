#Bank account
'''It's time to open up a bank account! 🏦

Create a file called bank_accounts.py.

Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

    first_name (string)
    last_name (string)
    account_id (integer)
    account_type (string)
    pin (integer)
    balance (float)

Next, let's create three methods:

    .deposit(): Add money into the account and return the new balance.
    .withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
    .display_balance(): Print the current value of balance.

Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

    Deposit $96 in the account.
    Withdraw $25 from the account.
    Print the current account balance.
'''
class BankAccount :
    def __init__(self, first_name, last_name, account_number, account_type, pin=0, balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.account_type = account_type
        self.pin =  pin
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount
        return self.balance
    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance -= ammount
            return ammount
        else:
            return("Insufficient funds")
    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

account  = BankAccount("Bill", "Tingly", 12345, "Checking", 1234, 0.0)
new_balance =account.deposit(96)
print(f"New Balance: ${new_balance:.2f}")
withdrawn_ammount = account.withdraw(25)
print(f"Ballance:  ${account.balance:.2f}")


'''# Bank Accounts 🏦
# Codédex

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"${self.balance}")

checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)

checking_account.deposit(100)

checking_account.display_balance()

checking_account.withdraw(50)

checking_account.display_balance()'''