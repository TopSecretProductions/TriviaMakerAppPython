#Trivia Maker program
#This program allows you to add questions into the questions.csv file
#the questions.csv file feeds the trivia program with questions
#The format should be:
#Column1: Question
#Column2-5: Possible answers (a thru c)
#Column6:  Correct answer (a thru c)
#This program should either create or open a csv called questions.csv
#it should prompt you to enter in a question, saved under column 1
#it should prompt you to enter in 4 possible answers, saved under column 2:5
#it should prompt you to mark which of those answers is correct (a, b, c, or d) under column 6
#it should be exited with the command "exit" or ctrl+c
#This iteration probably will not contain any data sanatization, though any public version should

#==============================================================================

print("#######                             #     #                              ")
print("   #    #####  # #    # #   ##      ##   ##   ##   #    # ###### #####  ")
print("   #    #    # # #    # #  #  #     # # # #  #  #  #   #  #      #    # ")
print("   #    #    # # #    # # #    #    #  #  # #    # ####   #####  #    # ")
print("   #    #####  # #    # # ######    #     # ###### #  #   #      #####  ")
print("   #    #   #  #  #  #  # #    #    #     # #    # #   #  #      #   #  ")
print("   #    #    # #   ##   # #    #    #     # #    # #    # ###### #    #")
print("Version 1.0")
print("by TopSecret\n\n\n")

#=======================================================================
#intro text

print("Welcome to Trivia Maker by TopSecret (Version 1.0)\n\n")
print("This program is designed to add questions into the CSV file that feeds Trivia by TopSecret")
print("The format of the CSV is as follows:\nColumn1: Question\nColumn2 through Column5: Possible answers\nColumn6: Letter of correct answer")
print("Follow the prompts on the screen to add new questions to the CSV")
print("To quit this program, type 'exit' as the field for the question or use ctrl+c")

#=================================================

#import libraries
import csv


#==================================================

with open('questions.csv', 'a', newline='') as questions:
    writerObject = csv.writer(questions)
    
    #Triggers program closing when "exit" is typed under the question column
    trigger = ["blank"]
    while trigger[0] != "exit":
        questionList = []
        question = input("\n\n\nWhat question would you like to ask?")
        if question == "exit" or question == "EXIT" or question == "Exit":
            trigger[0] = "exit"
            break
        #======================================================================
        #Take input from user to go in the CSV row
        answerA = input("\n\n\nNow is the time to type in possible answers.\na.)")
        answerB = input("\nb.)")
        answerC = input("\nc.)")
        answerD = input("\nd.)")
        ANSWER_OPTIONS = ["a", "b", "c", "d"] #hardcoded constant of answer options - limits answers to 4 options
        correctAnswer = "blank" #the next 3 lines of code confirm that a valid entry is entered for column 6
        while correctAnswer not in ANSWER_OPTIONS:
            correctAnswer = input("Which option is the correct answer? (please only type a, b, c, or d)").lower()
            
        #==========================================================
        #The following section adds all the user inputs into an empty list and then writes them to the CSV.
        #The loop repeats infinitely until "exit" is typed for a question or "ctrl+C" is pressed
        questionList.append(question)
        questionList.append(answerA)
        questionList.append(answerB)
        questionList.append(answerC)
        questionList.append(answerD)
        questionList.append(correctAnswer)
        writerObject.writerow(questionList)

