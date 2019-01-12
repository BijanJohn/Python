#Bijan Rahnamnai Syn: 26102
#Lab 6C
#Enter a winning powerball number and search for a match in the file
#Provide the winning number if it is found
#otherwise let the end user know that no records matched the winning powerball number
#7/11/2017

def main():
    #Create a bool variable to use as a flag
    found = False

    #Get the Search value
    search = input('Enter the winning Powerball number: ')
    try:
        #Open the powerball.txt file
        infile = open ('powerball.txt','r')

        #Read the first record's description field
        descr = infile.readline()
        
        #Read the rest of the file.
        while descr != '':
            
                #strip the \n from the end of the line
                descr = descr.rstrip('\n')

                #Determine whether this record matches the search value
                if descr == search:
                    #Display the record.
                    print('Winner Found:', descr)
                    print()
                    #Set the found flag to true
                    found = True

                #Read the next description.
                descr = infile.readline()

        #Close the file
        infile.close()

        if not found:
            print('That item was not found in the file.')

    except IOError:
        print('There was a problem with your file, please double check.')

    except:
        print('There was an error')
    

main()
