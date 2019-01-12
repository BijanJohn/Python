#Bijan Rahnamnai Syn: 26102
#Lab 6A
#Ask the user how many tickets they would like to buy
#only accept 1-10 # of tickets and ask the user if they want to play again
#print for Quick picks of sorted non-repeating numbersr from between 1 and 69
#and 1 powerball between 1 and 26 at the end
#open a file and append the numbers to the file
#close the file and print the records recorded to the file
#7/11/2017


import random

def main():
    play_again = 'y'
    while play_again == 'y':
        Powerball()
        print('\n')
        play_again = input('Do you want to play again? (enter "y" for yes)')

def Powerball():
    ticket =[]
    tries = 0
    ticketCount = int(input('How many powerball tickets would you like to buy? '))
    while ticketCount <= 0 or ticketCount >= 11:
        if tries ==2:
            print(('\n').center(28))
            print('        Sorry, this was your last attempt. Input should be between 1 and 10')
            print(('\n').center(28))
            break
        print(('\n').center(28))
        print('        Sorry, Input should be between 1 and 10.')
        print(('\n').center(28))
        ticketCount = int(input('How many powerball tickets would you like to buy? '))
        tries += 1
    file = open('powerball.txt','a')
    if ticketCount >= 1 and ticketCount <= 10:
        for n in range(ticketCount):
            PB = random.randint(1,26)
            ticket = sorted(random.sample(range(1,69),5))
            a = ticket[0]
            b = ticket[1]
            c = ticket[2]
            d = ticket[3]
            e = ticket[4]
            print(str(a).zfill(2), str(b).zfill(2), str(c).zfill(2), str(d).zfill(2), str(e).zfill(2), str(PB).zfill(2))

            for item in ticket:
                file.write(str(item).zfill(2) + ' ')
            file.write(str(PB).zfill(2) + '\n')
    file.close()
    if ticketCount >= 1 and ticketCount <= 10:
        print('All records processed and written to file.')

main()
