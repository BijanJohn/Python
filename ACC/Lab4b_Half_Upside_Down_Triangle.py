#Bijan Rahnamai
#Lab 4 B - Extra Credit Assignment
#This program will create a half inverted traingle using loops
#The solution will look like the following
#6/18/2017

#**********
#*********
#********
#*******
#******
#*****
#****
#***
#**
#*

print ("\n" * 50)
a = 10

for r in range (10):
    for c in range (r):
        a = 10 - r
    print ('*'*a)
print ()
