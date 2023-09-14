
#=============================================
#importing libraries
import csv
import time
#=============================================
print("#######                             #                   ")
print("   #    #####  # #    # #   ##     # #   #####  #####  ")
print("   #    #    # # #    # #  #  #   #   #  #    # #    # ")
print("   #    #    # # #    # # #    # #     # #    # #    # ")
print("   #    #####  # #    # # ###### ####### #####  #####  ")
print("   #    #   #  #  #  #  # #    # #     # #      #      ")
print("   #    #    # #   ##   # #    # #     # #      #   ")
time.sleep(1)
print("Produced by:...")
time.sleep(1)
print("'TopSecret'")
time.sleep(1)
print("(Version 1.0.1)")
time.sleep(1)

#=====================================================
print("\n\n\n\nWelcome to TriviaApp v1.0.1 by 'TopSecret'")
print("This app pulls questions from questions.csv in triviaApp directory.")
print("I hope you've loaded your CSV with lots of great trivia using the TriviaMaker App!  \nOr, you could go to our website and try one of our great loaded trivia CSVs!.")
print("You can exit anytime by pressing ctrl+C.")
time.sleep(8)

#creating scoreboard - score[0] == number of correct answers, score[1] == number of questions answered
score = [0, 0]

#==============================================
#opening and reading one row at a time from CSV file
with open('questions.csv', 'r') as questions:
    questionsReader = csv.reader(questions)
    for row in questionsReader:
        
        print("\n\nCurrent Score: " + str(score[0]) + "/" + str(score[1]))
        #formatting multiple choice question
        print("Question: \n" + row[0]+"\n\n")
        print("a.)" + row[1]+ "\n")
        print("b.)" + row[2]+ "\n")
        print("c.)" + row[3]+ "\n")
        print("d.)" + row[4]+ "\n")
        
        #applying answer logic
        answerBank = ["a", "b", "c", "d"]
        answer = "blank"
        while answer not in answerBank:
            answer = input("Answer:").lower()
        if answer == row[5]:
            score[0] += 1
        score[1] += 1
        time.sleep(.5)
        print("====================================")
    

    #csv file closes automatically with with() function
    #calculating final score
    grade = round((score[0] / score[1]) * 100, 1)
    print("\n\n\n")
    if grade >= 70:
        print("#####    ##    ####   #### ") 
        print("#    #  #  #  #      #      ")
        print("#    # #    #  ####   ####  ")
        print("#####  ######      #      # ")
        print("#      #    # #    # #    # ")
        print("#      #    #  ####   #### ")
    else:
        print("######   ##   # #   ")   
        print("#       #  #  # #     ") 
        print("#####  #    # # #      ")
        print("#      ###### # #      ")
        print("#      #    # # #      ")
        print("#      #    # # ###### ")
    time.sleep(2)
    print("\n\n\nYou scored " + str(grade) + "%\n\n\n" )
    time.sleep(2)


        
