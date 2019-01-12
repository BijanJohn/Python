#Bijan Rahnamai SYN: 26102
#Lab 7
#The program assumes that the student's solutions are listed such
#that each line includes the student's answer to the question,
#without the question number preceding the answer. The student's
#answers are assumed to be in the order of the questions.
#7/13/2017


def main():
    #Setup Variables
    solution = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

    correct_counter = 0

    incorrect_counter = 0

    incorrect_questions = []

    counter = 0

    try:
        file_name = input('Enter a valid file name: ')
        #open the file for reading
        file_answers = open(file_name)
        #Read all the lines in the file into a list
        answers = file_answers.readline()
        file_answers.close()

        index = 0
        while index < len(answers):
            #Strip trailing '\n' from all elements of the list.
            answers = [line.rstrip() for line in open(file_name)]

            index += 1
        #Compare student solution to correct solution and update
        #appropriate counters.
        for i in range(len(solution)):
            if answers[i] == solution[i]:
                correct_counter += 1
            else:
                incorrect_counter += 1
        #Determine if student passed and display result.
        if correct_counter >= 15:
            print('You passed the Exam')
        else:
            print('You failed the Exam')
        #Display exam details.
        print('Number of Correct Answers: ', correct_counter)
        print('Number of Correct Answers: ', incorrect_counter)
    
        #Determine if the student got any questions wrong.
        for i in range(len(solution)):
            if answers[i] != solution[i]:
                incorrect_questions.append(i + 1)

                string = ""

                for item in incorrect_questions:
                    string += str(item) + ", "
                
        print('Questions you answered incorrectly:', string[:-2])
        
    #Handle any errors that may occur.
        
    except IOError:
        print('The file could not be found.')
    except IndexError:
        print('There was an indexing error.')
    except:
        print('An error occured.')
main()
