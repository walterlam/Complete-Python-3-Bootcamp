# 05 OOP Challenge

'''
For this challenge, create a bank account class that has two attributes:
- owner
- balance
and two methods:
- deposit
- withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.
'''

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner:   {self.owner}' + '\n' +\
               f'Account balance: ${self.balance}'
    
    def deposit(self,amount):
        self.balance += amount
        print('Deposit accepted')
    
    def withdraw(self,amount):
        if self.balance < amount:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print('Withdrawal accepted')
               
