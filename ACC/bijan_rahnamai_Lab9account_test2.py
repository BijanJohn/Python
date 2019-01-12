#Bijan Rahnamai SYN:26102
#Lab Assignment 9
#7/31/2017
# This program demonstrates the BankAccount class
# with the __str__ method added to it.
# It contains a loop and try/except clause

import bijan_rahnamai_Lab9bankaccount2

def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('\n')
        print('Welcome to the Banking System.')
        # Get the starting balance.
        start_bal = float(input('Enter your starting balance: '))
        savings = bijan_rahnamai_Lab9bankaccount2.BankAccount(start_bal)

        # Deposit the user's paycheck.
        try:
            pay = float(input('How much were you paid this week? '))
            print('I will deposit that into your account.')
            savings.deposit(pay)
            
        except:
            print('An error occured')
            
        # Display the balance.
        print(savings)

            # Get the amount to withdraw.
        try:
            cash = float(input('How much would you like to withdraw? '))
            print('I will withdraw that from your account.')
            savings.withdraw(cash)
        except:
            print('An error occured')
            
        # Display the balance.
        print(savings)
        again = input('Do you want to access the Banking System again? (y/n)')
# Call the main function.
main()
