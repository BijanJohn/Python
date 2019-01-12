#Bijan Rahnamai SYN:26102
#Lab Exercise 5A
#In this lab I will build upon a previous lab including a menu for options to convert data
#and using functions to call the necessary tasks
#6/26/2017

US_TO_UK = 1
UK_TO_US = 2
QUIT_CHOICE = 3

def main():

    choice = 0
    display_menu()
    choice = int(input('Enter your choice: '))
        
    if choice == US_TO_UK:
        miles = float(input('Hello, please tell me what distance in miles \
that you want me to convert to kilometers: '))
        milesToKm(miles)
        fahrenheit = float(input('Hello, please tell me what temperature \
in fahrenheit that you would like me to convert \
to celsuis: '))
        FahToCel(fahrenheit)
        gallons = float(input('Hello, please tell me how many gallons \
you would like me to convert to liters: '))
        GalToLit(gallons)
        pounds = float(input('Hello, please tell me how many pounds \
you would like me to convert to kilograms: '))
        PoundsToKg(pounds)
        inches = float(input('Hello, please tell me how many inches \
you would like me to convert to centimeters: '))
        InchesToCm(inches)
    elif choice == UK_TO_US:
        kilometers = float(input('Hello, please tell me what distance in kilometers \
that you want me to convert to miles: '))
        KmToMiles(kilometers)
        Celsius = float(input('Hello, please tell me what temperature \
in celsius that you would like me to convert \
to fahrenheit: '))
        CelToFah(Celsius)
        liters = float(input('Hello, please tell me how many liters \
you would like me to convert to Gallons: '))
        LitToGal(liters)
        kilograms = float(input('Hello, please tell me how many kilograms \
you would like me to convert to pounds: '))
        KgToPounds(kilograms)
        centimeters = float(input('Hello, please tell me how many centimeters \
you would like me to convert to inches: '))
        CmToInches(centimeters)        
    elif choice == QUIT_CHOICE:
        print('Exiting the program.')
    else:
        print('Error: invalid selection.')
            
#This is the menu display function
def display_menu():
    print('Hello, in this program we will convert measurements for different countries')
    print('Please select from the following menu:')
    print('Enter 1 to Convert US to UK')
    print('Enter 2 to Convert UK to US')
    print('Enter 3 to Quit')

#These are the US to UK Functions        
def milesToKm(miles):
    tries = 0
    while miles <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        miles = float(input('Hello, please tell me what distance in miles \
that you want me to convert to kilometers: '))
        tries += 1
    if miles > 0:
        milesToKilometers = miles * 1.6
        print ('Hello,', miles, 'miles is equal to '\
        , format (milesToKilometers, '.1f'), 'kilometers. \nIsn\'t that interesting!')
        print ('\n')

def FahToCel(fahrenheit):
    tries = 0
    while fahrenheit > 1000:
        if tries == 2:
            print('Sorry, a temperature greater than 1000 degrees won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, a temperature greater than 1000 degrees won\'t be accepted.')
        print (' ')
        fahrenheit = float(input('Hello, please tell me what temperature \
in fahrenheit that you would like me to convert \
to celsuis: '))
        tries += 1
    if fahrenheit <= 1000:
        fahrenheitToCelcius = (fahrenheit - 32)* 5/9
        print ('Hello,', fahrenheit, 'degrees in fahrenheit is equal to'\
       , format (fahrenheitToCelcius, '.1f'), 'degrees in celcius.')
        print('Isn\'t that awesome!')
        print ('\n')

def GalToLit(gallons):
    tries = 0
    while gallons <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        gallons = float(input('Hello, please tell me how many gallons \
you would like me to convert to liters: '))
        tries += 1
    if gallons > 0:
        gallonsToLiters = (gallons * 3.9)
        print ('Hello,', gallons, 'gallons is equal to '\
       , format (gallonsToLiters, '.1f'), 'liters.')
        print ('\n')
    
def PoundsToKg(pounds):
    tries = 0
    while pounds <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        pounds = float(input('Hello, please tell me how many pounds \
you would like me to convert to kilograms: '))
        tries += 1
    if pounds > 0:
        poundsToKilograms = (pounds * .45)
        print ('Hello,', pounds, 'pounds is equal to '\
       , format (poundsToKilograms, '.2f'), 'kilograms.')
        print ('\n')

def InchesToCm(inches):
    tries = 0
    while inches <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        inches = float(input('Hello, please tell me how many inches \
you would like me to convert to centimeters: '))
        tries += 1
    if inches > 0:  
        inchesToCentimeters = (inches * 2.54)
        print ('Hello,', inches, 'inches is equal to '\
       , format (inchesToCentimeters, '.2f'), 'centimeters.')
        print ('\n')

#These are the UK to US Functions
def KmToMiles(kilometers):
    tries = 0
    while kilometers <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        kilometers = float(input('Hello, please tell me what distance in kilometers \
that you want me to convert to miles: '))
        tries += 1
    if kilometers > 0:
        KmToMiles = kilometers / 1.6
        print ('Hello,', kilometers, 'kilometers is equal to '\
        , format (KmToMiles, '.1f'), 'miles. \nIsn\'t that interesting!')
        print ('\n')

def CelToFah(celsius):
    tries = 0
    while celsius > 1000:
        if tries == 2:
            print('Sorry, a temperature greater than 1000 degrees won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, a temperature greater than 1000 degrees won\'t be accepted.')
        print (' ')
        celsius = float(input('Hello, please tell me what temperature \
in celsius that you would like me to convert \
to fahrenheit: '))
        tries += 1
    if celsius <= 1000:
        CelToFah = (celsius * 9/5)+ 32
        print ('Hello,', celsius, 'degrees in celcius is equal to'\
       , format (CelToFah, '.1f'), 'degrees in fahrenheit.')
        print('Isn\'t that awesome!')
        print ('\n')

def LitToGal(liters):
    tries = 0
    while liters <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print (' ')
        liters = float(input('Hello, please tell me how many liters \
you would like me to convert to gallons: '))
        tries += 1
    if liters > 0:
        LitToGal = (liters / 3.9)
        print ('Hello,', liters, 'liters is equal to '\
       , format (LitToGal, '.1f'), 'gallons.')
        print ('\n')
    
def KgToPounds(kilograms):
    tries = 0
    while kilograms <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        kilograms = float(input('Hello, please tell me how many kilograms \
you would like me to convert to pounds: '))
        tries += 1
    if kilograms > 0:
        KgToPounds = (kilograms / .45)
        print ('Hello,', kilograms, 'kilograms is equal to '\
       , format (KgToPounds, '.2f'), 'pounds.')
        print ('\n')

def CmToInches(centimeters):
    tries = 0
    while centimeters <= 0:
        if tries == 2:
            print('Sorry, negative or zero values won\'t be accepted. \
This was your last attempt.')
            break
        print('Sorry, negative or zero values won\'t be accepted.')
        print(' ')
        centimeters = float(input('Hello, please tell me how many centimeters \
you would like me to convert to inches: '))
        tries += 1
    if centimeters > 0:  
        CmToInches = (centimeters / 2.54)
        print ('Hello,', centimeters, 'centimeters is equal to '\
       , format (CmToInches, '.2f'), 'inches.')
        print ('\n')
        
main()
