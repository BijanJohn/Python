#Bijan Rahnamai
#Lab 4 Part C
#In this program I will ask for grades of a student and display the numeric grade as a letter grade
#I will keep a running total of the numeric grades entered
#I will issue a message based upon the grade entered
#I will caculate the class average at the end, unless no grades were entered
#6/19/2017

#First, call the main functioon
def main():

#Initialize the variables and start the loop
    moreStudent = 'y'
    totalGrades = 0.0
    gradeCount = 0.0
    average = 0.0

#Next, print the introduction command
    print('Hello Professor, time to calculate some grades.')
    print('-----------------------------------------------')

#Start the conditioned loop
    while moreStudent =='y':
#Ask for input
        grade = float(input('Please enter a grade or a -1 to end: '))
#While the input doesn't equal -1 caculate the letter grade
        while grade != -1:
            if grade >= 90 and grade <= 100:
                print('You got an A. Thats awesome.')
                print('\n')
            elif grade >= 80 and grade <= 89:
                print('You got a B. Thats pretty good.')
                print('\n')
            elif grade >= 70 and grade <= 79:
                print('You got a C. Thats Ok.')
                print('\n')
            elif grade >= 60 and grade <= 69:
                print('You got a D. That is passing.')
                print('\n')
            elif grade >= 0 and grade <= 59:
                print('You made an F! Obviously you did not study!')
                print('\n')
            else:
                print('You must enter a grade between 0 and 100.')
                print('\n')
#Caculate the total grades, the grade count and the average
            totalGrades += grade
            gradeCount += 1
            average = totalGrades / gradeCount
#Ask for more input
            grade = float(input('Enter the next grade or -1 to end: '))
#If no grade was ever entered let the user know and break the program            
        if (grade == -1) and (gradeCount == 0.0):
            print('No grades were entered')
            break
#If no more grades are present, ask if there is another student
        if (grade == -1) and (gradeCount != 0.0):
            moreStudent = input('Are you a new student and ready to enter your grades? y or n: ')
#If no more students are present then show the average and number of grades entered, and close the program
    while moreStudent == 'n':
        print('The class average is ',format(average,'.2f'))
        print('The number of grades entered was ',int(gradeCount))
        break
#Call the main function
main()
