#Bijan Rahnamai SYN:26102
#Lab Exercise 3a
#In this lab I will convert Imperial data into Metric Data 
#Based on the input entered by the end user
#I will also ensure that end user cannot enter a negative number for all 5 equations
#Except for the Temperature Calculation, for the temperature calculation I will not accept a temperature
#above 1000 degrees in Fahrenheit
#The User will have 3 attempts for each of the sections
#6/10/2017

def main():

#This section will convert Miles to Kilometers
#First by prompting the user to input a distance, then processing the data
#and the returning the value of the distance in Kilometers
    print ("\n" * 50)
#Here I will initialize the loop    
    tries = 0
    miles = float(input('Hello, please tell me what distance in miles \
that you want me to convert to Kilometers: '))
#Here the user has 3 attempts before breaking the program
    while miles <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        miles = float(input('Hello, please tell me what distance in miles \
that you want me to convert to Kilometers: '))
        tries += 1
    if miles > 0:
        milesToKilometers = miles * 1.6
        print ('Hello,', miles, 'miles is equal to '\
        , format (milesToKilometers, '.1f'), 'kilometers. \nIsn\'t that interesting!')
        print ('\n')

#This section will convert Fahrenheit to Celsius
#First by prompting the user to input a temperature, then processing the data
#and the returning the value of the temperature in Celcius
#Here I will initialize the loop
    tries = 0
    fahrenheit = float(input('Hello, please tell me what temperature \
in Fahrenheit that you would like me to convert \
to Celsuis: '))
#Here the user has 3 attempts before breaking the program
    while fahrenheit > 1000:
        if tries == 2:
            print('Sorry, a temperature greater than 1000 degrees won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, a temperature greater than 1000 degrees won\'t be accepted.')
        print (' ')
        fahrenheit = float(input('Hello, please tell me what temperature \
in Fahrenheit that you would like me to convert \
to Celsuis: '))
        tries += 1
    if fahrenheit <= 1000:
        fahrenheitToCelcius = (fahrenheit - 32)* 5/9
        print ('Hello,', fahrenheit, 'degrees in Fahrenheit is equal to'\
       , format (fahrenheitToCelcius, '.1f'), 'degrees in Celcius.')
        print('Isn\'t that awesome!')
        print ('\n')
    
#This section will convert Gallons to Liters
#First by prompting the user to input an amount in Gallons, then processing the data
#and the returning the value of the amount in Liters
#Here I will initialize the loop   
    tries = 0
    gallons = float(input('Hello, please tell me how many Gallons \
you would like me to convert to Liters: '))
#Here the user has 3 attempts before breaking the program
    while gallons <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        gallons = float(input('Hello, please tell me how many Gallons \
you would like me to convert to Liters: '))
        tries += 1
    if gallons > 0:
        gallonsToLiters = (gallons * 3.9)
        print ('Hello,', gallons, 'gallons is equal to '\
       , format (gallonsToLiters, '.1f'), 'liters.')
        print ('\n')

#This section will convert Pounds to Kilograms
#First by prompting the user to input an amount in Pounds, then processing the data
#and the returning the value of the amount in Kilograms
#Here I will initialize the loop   
    tries = 0
    pounds = float(input('Hello, please tell me how many Pounds \
you would like me to convert to Kilograms: '))
#Here the user has 3 attempts before breaking the program
    while pounds <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        pounds = float(input('Hello, please tell me how many Pounds \
you would like me to convert to Kilograms: '))
        tries += 1
    if pounds > 0:
        poundsToKilograms = (pounds * .45)
        print ('Hello,', pounds, 'pounds is equal to '\
       , format (poundsToKilograms, '.2f'), 'kilograms.')
        print ('\n')

#This section will convert Inches to Centimeters
#First by prompting the user to input a length in Inches, then processing the data
#and the returning the value of the length in Centimeters
#Here I will initialize the loop
    tries = 0
    inches = float(input('Hello, please tell me how many Inches \
you would like me to convert to Centimeters: '))
#Here the user has 3 attempts before breaking the program
    while inches <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        inches = float(input('Hello, please tell me how many Inches \
you would like me to convert to Centimeters: '))
        tries += 1
    if inches > 0:  
        inchesToCentimeters = (inches * 2.54)
        print ('Hello,', inches, 'inches is equal to '\
       , format (inchesToCentimeters, '.2f'), 'centimeters.')
        print ('\n')

#This will Call the main function to run the program.
main()
