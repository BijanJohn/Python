#Bijan Rahnamai SYN: 26102
#Lab 5B
#This program will generate powerball numbers for playing the lottery
#The user will input how many tickets they want and the program will only allow 1-10 tickets
#6/26/2017

#Import the random and datetime modules
import random
from datetime import datetime

#define the main function, this function will take in the other receive_input function and the powerball function.
def main():
    play_a_game = 'y'
    print(('\n').center(28))
    #Ask if the user wants to play a game
    play_a_game = input("          Do you want to play a game:'y' or 'n': ")
    #The while loop will continue until the user exits the program
    while play_a_game == 'y':
        #Print the intro
        print('\n'*50)
        print("    Welcome to the automated Powerball QuickPick Provider!")
        print("        Here you may purchase up to 10 QuickPick numbers.")
        print("     QuickPicks are provided at a rate of $2.00 per play.")
        print('\n')
        #Get the number of times the program should be run
        #Apply the input
        number_of_times = receive_input()
        #If the input is not valid break the program.
        if number_of_times <= 0 or number_of_times >= 11:
            break
        #Store the values in the list
        tickets = []
        alpha = ['A.','B.','C.','D.','E.','F.','G.','H.','I.','J.']
        try:
            for n in range(number_of_times):
                #Call the Powerball function
                tickets = Powerball()
                print('                ','QP',alpha[n],format(tickets[0],'02d'),format(tickets[1],'02d'),format(tickets[2],'02d'),format(tickets[3],'02d'),format(tickets[4],'02d')\
                ,('[PB]'),format(tickets[5],'02d'))
            if number_of_times != 0:
                cost = number_of_times * 2
                print('                        Cost: $',format(cost,'.2f'))
                print((datetime.now().strftime("                  Printed: %m-%d-%y %H:%M:%S")).center(28))
                print(('\n').center(28))
            play_a_game = input("          Do you want to play a game:'y' or 'n': ")
        except TypeError:
            print('        Sorry, Input should be between 1 and 10.')
        except:
            print('        Sorry, Input should be between 1 and 10.')
        if play_a_game != 'y':
            break
    if play_a_game == 'n':
        print(('\n').center(28))
        print('Thanks! We will see you next time!')
#The receive_input function prompts the user to enter a number of tickets
#if it is not 1-10 then it will present an error
#it returns the value afterwards to the main function.
def receive_input():
    number_lines = int(input('        Input desired number of QuickPicks: (only 1-10): '))
    tries = 0
    while number_lines <= 0 or number_lines >= 11:
        if tries == 2:
            print(('\n').center(28))
            print('        Sorry, this was your last attempt. Input should be between 1 and 10')
            print(('\n').center(28))
            return number_lines
        print(('\n').center(28))
        print('        Sorry, Input should be between 1 and 10.')
        print(('\n').center(28))
        number_lines = int(input('        Input desired number of QuickPicks: (only 1-10): '))
        tries += 1
    if number_lines >= 1 and number_lines <= 10:
        return number_lines 
#The Powerball function calculates the 5 non repeating random numbers in ascending order
#Followed by the random Powerball number
#it returns the 6 values afterwards back to the main function
def Powerball():
    result = []
    #selecting first 5 random non-repeating balls
    for i in range(5):
        number = random.randint(1,69)
        while(number in result):
            number = random.randint(1,69)
        result.append(number)
    result.sort()
    #Powerball number selected
    result.append(random.randint(1,26))
    return result
#Call the main function
main()
