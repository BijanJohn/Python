# This program displays the contents
# of a file if found, otherwise create a new file

def main():
    # Get the name of a file.
    Customer_name = input('Please enter Name of Customer: ')
    filename = Customer_name + '.txt'
    print (filename)
    try:
        # Open the file.
        infile = open(filename, 'r')
          
        # Read the file's contents.
        contents = infile.read()

        # Display the file's contents.
        print(contents)

        # Close the file.
        infile.close()
        
    except IOError:
        print('Existing customer record NOT found')
        print('Creating new customer record', filename)
        outfile = open(filename, 'w')
        outfile.write ('6000\n')
        outfile.close()
    except:
        print('An error occurred')


# Call the main function.
main()

