print("#######                             #                   ")
print("   #    #####  # #    # #   ##     # #   #####  #####  ")
print("   #    #    # # #    # #  #  #   #   #  #    # #    # ")
print("   #    #    # # #    # # #    # #     # #    # #    # ")
print("   #    #####  # #    # # ###### ####### #####  #####  ")
print("   #    #   #  #  #  #  # #    # #     # #      #      ")
print("   #    #    # #   ##   # #    # #     # #      #   ")
print("by TopSecret (Version 1.0)")


print("\n\n\n\nWelcome to TriviaApp by TopSecret (Version 1.0).")
print("This app pulls questions from questions.csv in this same folder.")
print("You can exit anytime by typing 'exit' or by pressing ctrl+C.")

#=============================================
#importing libraries
import csv

#=============================================
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
    print("\n\n\nYou scored " + str(grade) + "%\n\n\n" )


        
