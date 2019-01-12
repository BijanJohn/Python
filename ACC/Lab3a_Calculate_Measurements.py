#Bijan Rahnamai SYN:26102
#Lab Exercise 3a
#In this lab I will convert Imperial data into Metric Data 
#Based on the input entered by the end user
#I will also ensure that end user cannot enter a negative number for all 5 equations
#Except for the Temperature Calculation, for the temperature calculation I will not accept a temperature
#above 1000 degrees in Fahrenheit
#6/10/2017

def main():

#This section will convert Miles to Kilometers
#First by prompting the user to input a distance, then processing the data
#and the returning the value of the distance in Kilometers
    print ("\n" * 50)
    miles = float(input('Hello, please tell me what distance in miles \
that you want me to convert to Kilometers: '))

    milesToKilometers = miles * 1.6

    if miles <= 0:
        print('Sorry, negative or zero values won\'t be accepted.')
        print ('\n')
    else:    
        print ('Hello,', miles, 'miles is equal to '\
        , format (milesToKilometers, '.1f'), 'kilometers. \nIsn\'t that interesting!')
        print ('\n')

#This section will convert Fahrenheit to Celsius
#First by prompting the user to input a temperature, then processing the data
#and the returning the value of the temperature in Celcius
    fahrenheit = float(input('Hello, please tell me what temperature \
in Fahrenheit that you would like me to convert \
to Celsuis: '))

    fahrenheitToCelcius = (fahrenheit - 32)* 5/9

    if fahrenheit > 1000:
        print('Sorry, a temperature greater than 1000 degrees won\'t be accepted.')
        print ('\n')
    else:
        print ('Hello,', fahrenheit, 'degrees in Fahrenheit is equal to'\
       , format (fahrenheitToCelcius, '.1f'), 'degrees in Celcius.')
        print('Isn\'t that awesome!')
        print ('\n')
    
#This section will convert Gallons to Liters
#First by prompting the user to input an amount in Gallons, then processing the data
#and the returning the value of the amount in Liters
    gallons = float(input('Hello, please tell me how many Gallons \
you would like me to convert to Liters: '))

    gallonsToLiters = (gallons * 3.9)

    if gallons <= 0:
        print('Sorry, negative or zero values won\'t be accepted.')
        print ('\n')
    else:
        print ('Hello,', gallons, 'gallons is equal to '\
       , format (gallonsToLiters, '.1f'), 'liters.')
        print ('\n')

#This section will convert Pounds to Kilograms
#First by prompting the user to input an amount in Pounds, then processing the data
#and the returning the value of the amount in Kilograms
    pounds = float(input('Hello, please tell me how many Pounds \
you would like me to convert to Kilograms: '))

    poundsToKilograms = (pounds * .45)
    
    if pounds <= 0:
        print('Sorry, negative or zero values won\'t be accepted.')
        print('\n')
    else:
        print ('Hello,', pounds, 'pounds is equal to '\
       , format (poundsToKilograms, '.2f'), 'kilograms.')
        print ('\n')

#This section will convert Inches to Centimeters
#First by prompting the user to input a length in Inches, then processing the data
#and the returning the value of the length in Centimeters
    inches = float(input('Hello, please tell me how many Inches \
you would like me to convert to Centimeters: '))

    inchesToCentimeters = (inches * 2.54)

    if inches <= 0:
        print('Sorry, negative or zero values won\'t be accepted.')
        print('\n')
    else:
        print ('Hello,', inches, 'inches is equal to '\
       , format (inchesToCentimeters, '.2f'), 'centimeters.')
        print ('\n')

#This will Call the main function to run the program.
main()
