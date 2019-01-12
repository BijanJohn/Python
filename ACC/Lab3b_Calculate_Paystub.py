#Bijan Rahnamai SYN:26102
#Lab Exercise 3B
#In this exercise the program will ask for information about an employee
#In order to provide the details of the employee's paycheck
#6/10/2017

#First, Understand the requirements

#Second, Call the main function and print the Welcome message of the Program
def main():
    print("\n"*50)
    print("Welcome to the SoftwarePirates, Inc. salesforce paycheck calculator.")
    print("Please enter the following information to calculate the salesperson's paycheck:")

#Third, Declare the constants
    baseSalary = 2000

#Fourth, Get the Inputs
#Get the Sales Person Name
    name = str(input("Enter the Name of the Employee: "))
#Get the number of months the employee has worked in months
    time = int(input("Enter the employee's time with the company (in months): " ))
#Get the amount of sales the employee has had
    sales = float(input("Enter total sales for the employee: "))
#Get the number of days the employee has had for vacation
    vacation = int(input("Enter total number of vacation days used by employee: "))

    print("--------------------------------------------")
    print("\n"*5)

#Fifth, caculate the processes to data for the outputs    
    #Bonus and additional bonus if employee has been with company LONGER than 5 years (60 months)
    if time >= 60:
        if sales >= 1000000:
            altBonus = 1000
            bonus = 100000
        elif sales < 1000000 and sales >=500001:
            altBonus = 1000
            bonus = 5000
        elif sales < 500000 and sales >=100001:
            altBonus = 1000
            bonus = 1000
        else:
            altBonus = 0
            bonus = 0

    #Bonus if employee has been with the company less than 5 years but more than 3 months
    elif time < 60 and time >= 3:
        if sales >= 1000000:
            altBonus = 0
            bonus = 100000
        elif sales < 1000000 and sales >=500001:
            altBonus = 0
            bonus = 5000
        elif sales < 500000 and sales >=100001:
            altBonus = 0
            bonus = 1000
        else:
            altBonus = 0
            bonus = 0

    #If the employee has been with the company less than 3 months
    elif time < 3:
        altBonus = 0
        bonus = 0

    #Adjusts for vacation penalty
    if vacation >= 3:
        adjSalary = -200
    else:
        adjSalary = 0
              
    #Commission Calculation
    if sales > 1000000:
        commission = sales *.35
    elif sales <= 1000000 and sales >= 500001:
        commission = sales * .28
    elif sales <= 500000 and sales >= 100001:
        commission = sales * .15
    elif sales <= 100000 and sales >= 10000:
        commission = sales * .02
    else:
        commission = 0

#Sixth, finalize the last calulations              
    # Calculates the Total Salary
    totalSalary = baseSalary + (adjSalary + bonus + commission + altBonus)              

#Seventh, display the output like a real paycheck
    print("--------------------EMPLOYEE PAYSTUB--------------------")
    print("|                                                      |")           
    print("   Employee Name:                 ",name)
    print("|                                                      |")
    #Print the months employed
    print("   Time with Company in months:   ",time)
    print("|                                                      |")    
    #Print the Base Salary
    print("   Base Salary:                  $",format(baseSalary,',.2f'))
    print("|                                                      |")
    #Print the Commission earned (commission rate based on Sales)
    print("   Commission earned:            $",format(commission,',.2f'))
    print("|                                                      |")
    #Print the Bonus
    print("   Bonus earned:                 $",format(bonus,',.2f'))
    print("|                                                      |")
    #Print the Additional Bonus
    print("   Additional Bonus earned:      $",format(altBonus,',.2f'))
    print("|                                                      |")
    #print deductions
    print("   Deductions:                   $",format(adjSalary,',.2f'))
    print("|                                                      |")
    #print the total paycheck              
    print("   Total Gross Paycheck:         $",format(totalSalary,',.2f'))
    print("--------------------------------------------------------")

#Lastly, call the main function
main()
