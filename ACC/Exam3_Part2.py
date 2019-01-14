#Bijan Rahnamai SYN:26102
#Lab Assignment 9
#7/31/2017
# This program demonstrates the BankAccount class
# with the __str__ method added to it.
# It contains a loop and try/except clause
# It has a menu for 5 different options listed as the global constants
# It also will tell the user how many times they overdrafted

#Import the driver file and datetime modules
import Lab9bankaccount2_Bank_Class
from datetime import datetime

print('\n'*50)

#Declare the global constants
DEPOSIT = 1
WITHDRAW = 2
BALANCE = 3
OVERDRAFT = 4
QUIT = 5

#create the date function
date =((datetime.now().strftime("%m/%d/%y %H:%M:%S")))

#Define the main function
def main():
    global filename
    #Get the name of a file.
    print('\n')
    print('Welcome to the Banking System.')
    customer_name = input ('Please enter your name: ')
    while customer_name.isalpha() == False:
        print("Your name cannot contain digits or spaces.")
        print()
        customer_name = input('Please enter your name: ')
    filename = customer_name+'.txt'
    try:
        #open the file
        infile = open(filename, 'r')
        for line in infile:
            pass
        last=line
        print(filename+'\n')

        #Close the file.
        infile.close()

        #Display the file's contents
        print('Current balance for', customer_name+':')
        print('$'+last)
        line1=float(last)
        file = open(filename,'a')
        savings = Lab9bankaccount2_Bank_Class.BankAccount(line1)
        #Display the menu.
        choice = 0
        while choice!= QUIT:
            intro()
            #Get the user's choice for the menu
            choice = int(input('Enter your choice: '))
            # Get the amount to deposit. Display how much was given and what the balance now is on this current date/time.
            if choice == DEPOSIT:
                file = open(filename,'a')
                pay = float(input('How much would you like to deposit?: '))
                if savings.deposit(pay) == True:
                    file.write(str('You deposited ')+str(pay)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    print(('You deposited ')+str(pay)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    file.close()
                elif savings.deposit(pay) == False:
                    print('Sorry, values of 0 or less are not accepted')
            # Get the amount to withdraw. Display how much was taken and what the balance now is on this current date/time.
            elif choice == WITHDRAW:
                cash = float(input('How much would you like to withdraw?: '))
                if savings.withdraw(cash):
                    file = open(filename,'a')
                    file.write(str('You withdrew ')+str(cash)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    print(('You withdrew ')+str(cash)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)))
                    file.close()
                else:
                    print('You cannot withdraw a negative balance')
            # Display the balance.
            elif choice == BALANCE:
                print(str('Your balance is '),savings,str('$')+str(' on '+str(date)+str('\n')))
            #Calculate and display the latest overdraft attempts
            elif choice == OVERDRAFT:
                counter = 0
                file = open(filename,'r')
                for line in file:
                    if ('-') in line:
                        counter += 1
                print(str('There are ')+str(counter)+str(' overdraft attempts recently.'))
                file.close()
            #Quit the program
            elif choice == QUIT:
                file = open(filename,'a')
                print('Exiting the program.')
                #Write the last balance to the end of the file
                file.write(str(savings) + str('\n'))
                file.close()
            else:
                print('Error: Invalid Selection.')
    except IOError:
        #If the file doesn't exist, create it and then read the file.
        file = open(filename,'a')
        file.write(str('6000' + '\n'))
        file.close()
        choice = 0
        infile = open(filename, 'r')
        for line in infile:
            pass
        last=line
        print(filename+'\n')
        infile.close()
        #Display the file's contents
        print('Current balance for', customer_name+':')
        print('$'+last)
        line1=float(last)
        file = open(filename,'a')
        savings = Lab9bankaccount2_Bank_Class.BankAccount(line1)
        #Display the menu.
        choice = 0
        while choice!= QUIT:
            intro()
            #Get the user's choice for the menu
            choice = int(input('Enter your choice: '))
            # Get the amount to deposit. Display how much was given and what the balance now is on this current date/time.
            if choice == DEPOSIT:
                file = open(filename,'a')
                pay = float(input('How much would you like to deposit '))
                if savings.deposit(pay) == True:
                    file.write(str('You deposited ')+str(pay)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    print(('You deposited ')+str(pay)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    file.close()
                elif savings.deposit(pay) == False:
                    print('Sorry, values of 0 or less are not accepted')
            # Get the amount to withdraw. Display how much was taken and what the balance now is on this current date/time.
            elif choice == WITHDRAW:
                cash = float(input('How much would you like to withdraw? '))
                if savings.withdraw(cash):
                    file = open(filename,'a')
                    file.write(str('You withdrew ')+str(cash)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)+str('\n')))
                    print(('You withdrew ')+str(cash)+str('$  The Balance is ')+str(savings)+str(' on '+str(date)))
                    file.close()
                else:
                    print('You cannot withdraw a negative balance')
            # Display the balance.
            elif choice == BALANCE:
                print(str('Your balance is '),savings,str('$')+str(' on '+str(date)+str('\n')))
            #Calculate and display the latest overdraft attempts
            elif choice == OVERDRAFT:
                counter = 0
                file = open(filename,'r')
                for line in file:
                    if ('-') in line:
                        counter += 1
                print(str('There are ')+str(counter)+str(' overdraft attempts recently.'))
                file.close()
            #Quit the program
            elif choice == QUIT:
                file = open(filename,'a')
                print('Exiting the program.')
                #Write the last balance to the end of the file
                file.write(str(savings) + str('\n'))
                file.close()
            else:
                print('Error: Invalid Selection.')
    except:
        print('There was an error.')
def intro():
    print('Menu')
    print('1) Deposit')
    print('2) Withdraw')
    print('3) Show current balance')
    print('4) Overdraft')
    print('5) Quit')

# Call the main function.
main()
