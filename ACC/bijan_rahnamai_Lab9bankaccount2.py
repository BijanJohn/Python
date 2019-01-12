#Bijan Rahnamai SYN:26102
#Lab Assignment 9
#7/31/2017
# The BankAccount class simulates a bank account.
# It doesn't allow for a 0$ deposit
# If a user withdraws and has a balance less than 10$ a warning is provided
# If the user continues past the warning it will charge the user 50$

class BankAccount:
    
    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.
    
    def __init__(self, bal):
        self.__balance = bal
        if bal == 0 or bal < 0:
            print('Sorry, values of 0 or less are not accepted')

    # The deposit method makes a deposit into the
    # account.

    def deposit(self, amount):
        self.__balance += amount
        if amount <= 0:
            return(False)
            print('Sorry, values of 0 or less are not accepted')
        elif amount > 0:
            return(True)

    # The withdraw method withdraws an amount
    # from the account.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            if self.__balance > 10:
                return(True)
            #If the balance is less than 10 after the withdraw, warn the user
        if self.__balance < 10:
            print('Caution, 10$ is the mandatory minimum, by going below 10$ you will be charged a 50$ penalty.')
            caution = input('continue? (y/n)')
            #If they decline the funds will not be withdrawn
            if caution == 'n':
                print('You have decided to not withdraw.')
                self.__balance += amount
                return(False)
            #If they proceed, they will be charged $50 and may go into insufficent funds.
            if caution == 'y' or caution == 'Y':
                print('You are being charged a 50$ penalty')
                self.__balance -= 50
                return(True)
        if self.__balance < amount:
            print('Error: Insufficient funds')

    # The get_balance method returns the
    # account balance.
    
    def __str__(self):
        return str(self.__balance)
