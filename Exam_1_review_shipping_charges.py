# Exam 1 Practice
#6/11/2017
#In this program I will write a program that helps calculate
#the shipping charges for a shipping company

#First, Define the main function and greet the user
def main():
    print('Hello, this is the Fast Freight Shipping Company')
    print('This program will help you calculate the cost of shipping')

#Second, gather the input of the weight of the package
    weight = float(input('Please enter your package\'s weight in pounds: '))

#Third, caculate the rate for the package
    if weight > 10:
        rate = 4.75
    elif weight < 10 and weight > 6:
        rate = 4.00
    elif weight < 6 and weight > 2:
        rate = 3.00
    else:
        rate = 1.50
        
#Fourth, calculate the cost of the package

    cost = weight * rate


#Lastly, print the results to the user and call the main function
    print('Your shipping costs will be: $',cost)
main()
