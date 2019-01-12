#Exam 1 Review question
#Question Number 14
#Bijan
#6/11/2017
#Caculate the BMI of a user based on input
#Let the user know how in shape they are

#First, define the main function and welcome the user
def main():
    print('Hello, welcome to the BMI Calcualtor.')
    print('In this program we will help you calculate your BMI')
    print('and let you know if your weight is optimal')

#Second, gather the input from the user
    height = int(input('Please enter your height in inches: '))
    weight = float(input('Please enter your weight in pounds: '))

#Third, calcualte the BMI
    bmi = weight * (703 / (height**2))

#Fourth, Display the user's BMI
    print('Your BMI is ', format(bmi,'.2f'))

#Fifth, let the user know what level they are at
    if bmi <= 25 or bmi >= 18.5:
        print('Your weight is Ideal!')
    elif bmi > 25:
        print('Your are overweight.')
    else:
        print('You are underweight.')

#Lastly, call the main function
main()
