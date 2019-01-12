#Bijan Rahnamnai Syn: 26102
#Lab 6B
#Read the powerball.txt file and print the records stored in the file
#if any errors occur provide exception handling to the end user
#7/11/2017

def main ():

  counter=0
  try:
    infile = open ('powerball.txt', 'r')

    number = infile.readline()
    number = number.rstrip('\n')

    while number != '':
        print (number)  
        number = infile.readline()
        number = number.rstrip('\n')
        counter = counter +1

    infile.close()
    print ("Number of Powerball numbers Generated = ", counter)

  except IOError:
    print('There was a problem with your file, please double check.')

  except:
    print('There was an error')
    

main ()
