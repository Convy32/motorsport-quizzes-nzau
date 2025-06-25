# NZ Motorsport Quiz

import time
import sys

# Quiz Dictionary
quiz = {
    1: {
        "question": "What year did Shane van Gisbergen win his first V8 Supercars title?",
        "options": "A. 2015, B. 2016, C. 2017, D. 2018",
        "answer": "B"
    },
    2: {
        "question": "How many races did he win that year?",
        "options": "A. 8, B. 9, C. 10, D. 11",
        "answer": "A"
    },
    3: {
        "question": "True or False: Scott Mclaughlin debuted in IndyCar the weekend after Bathurst?",
        "options": "A. True, B. False",
        "answer": "A"
    },
    4: {
        "question": "Where did he finish in this race?",
        "options": "A. P10, B. P17, C. P19, D. P22",
        "answer": "D"
    },
    5: {
        "question": "How many times has Brendon Hartley won the 24 Hours of Le Mans?",
        "options": "A. 1, B. 2, C. 3, D. 4",
        "answer": "C"
    },
    6: {
        "question": "Where did Liam Lawson get his best finish in F1?",
        "options": "A. Zandvoort, B. Bahrain, C. Barcelona, D. Monaco",
        "answer": "D"
    },
    7: {
        "question": "True or False: Scott Dixon was actually born in Australia?",
        "options": "A. True, B. False",
        "answer": "A"
    },
    8: {
        "question": "What is the gap between Scott Dixon's first and last IndyCar championship?",
        "options": "A. 7 Years, B. 11 Years, C. 15 Years, D. 17 Years",
        "answer": "D"
    },
    9: {
        "question": "How many championships has he won?",
        "options": "A. 5, B. 6, C. 7, D. 8",
        "answer": "B"
    },
    10: {
        "question": "What is Andre Heimgartner’s best V8SC Championship finish?",
        "options": "A. 7, B. 9, C. 11, D. 13",
        "answer": "A"
    },
    11: {
        "question": "How many times has Greg Murphy won Bathurst?",
        "options": "A. 2, B. 3, C. 4, D. 5",
        "answer": "C"
    },
    12: {
        "question": "Who did Jim Richards pair with to win the Bathurst 1000 in “Godzilla”?",
        "options": "A. Peter Brock, B. Mark Skaife, C. Steven Richards, D. Garth Tander",
        "answer": "B"
    },
    13: {
        "question": "Who has not won the 24 Hours of Lemans?",
        "options": "A. Brendon Hartley, B. Scott Dixon, C. Chris Amon, D. Bruce McLaren",
        "answer": "B"
    },
    14: {
        "question": "At what age did Chris Amon enter Formula 1?",
        "options": "A. 18, B. 19, C. 21, D. 22",
        "answer": "B"
    },
    15: {
        "question": "When was Bruce McLaren's final Formula 1 win?",
        "options": "A. 1969 German GP, B. 1970 Monaco GP, C. 1968 Belgian GP, D. 1969 Monaco GP",
        "answer": "C"
    },
    16: {
        "question": "How many years did it take Denny Hulme to become an F1 winner, and champion?",
        "options": "A. 1, B. 2, C. 3, D. 4",
        "answer": "B"
    },
    17: {
        "question": "Where was Earl Bamber born?",
        "options": "A. Pukekohe, B. Christchurch, C. Wanganui, D. Auckland",
        "answer": "C"
    },
    18: {
        "question": "How many GB3 races did Louis Sharp win to take the championship?",
        "options": "A. 2, B. 3, C. 4, D. 5",
        "answer": "D"
    },
    19: {
        "question": "How many Kiwis are currently racing in F1, Supercars, IndyCar and Nascar?",
        "options": "A. 8, B. 9, C. 10, D. 11",
        "answer": "C"
    },
    20: {
        "question": "How many New Zealand drivers have won the 24 Hours of Lemans?",
        "options": "A. 3, B. 5, C. 7, D. 9",
        "answer": "B"
    }
}

# Printing functions
def welcomer(test, delay = 0.0375): 
    for char in test:
        print(char, end ='', flush = True)
        time.sleep(delay)
    print()

def typer(test, delay = 0.05): 
    for char in test:
        print(char, end ='', flush = True)
        time.sleep(delay)
    print()

def printer(test, delay = 0.025): 
    for char in test:
        print(char, end ='', flush = True)
        time.sleep(delay)
    print()

# Welcome screen
welcomer("Welcome! This quiz is on Kiwis in Motorsport!")
time.sleep(0.375)
welcomer("Answer using just the letter of each option.")
time.sleep(0.375)
welcomer("Good Luck!")
time.sleep(0.75)
# Input to allow user to push enter to start. Variable is not used further
enterstart = input("Press Enter to Start!")
print("--------------------")

while True:
    # Reset the score
    score = 0
    # Loop through dictionary in order
    for q_num in quiz:
        # Gets the current question
        q = quiz[q_num]
        # Prints question and options
        printer(f"Q{q_num}: {q['question']}")
        typer(q['options'])
        # Define actual options to filter bad inputs
        valid_options = [opt.split('.')[0].strip().upper() for opt in q['options'].split(',')]

        # Ask for answer
        while True:
            answer = input("Your answer: ").strip().upper()
            if answer in valid_options:
                # Break to checking if answer is correct
                break
            else:
                # Print invalid and loop back
                print(f"Invalid Input. Please input a valid answer: {', '.join(valid_options)}")

        # Answer checker
        if answer == q['answer']:
            # Correct Answer
            print("Correct, Well Done!\n")
            # +1 to score
            score += 1
        else:
            # Incorrect Answer
            print(f"Incorrect, Bad Luck! The correct answer was {q['answer']}.\n")
    # End of quiz 
    welcomer(f"Quiz Complete, Well Done! You scored: {score} out of {len(quiz)}")
    time.sleep(1)
    # Ask to keep playing. kp = keep playing user input
    while True:
        welcomer("Would you like to play again?")
        time.sleep(0.5)
        kp = input("Y/N: ")
        if kp.upper() == "Y":
            # Start game again
            print("--------------------")
            welcomer("Welcome Back!")
            print("--------------------")
            # Breaking exits this loop and restarts the game loop
            break
        elif kp.upper() == "N":
            # Goodbye screen, exit game
            welcomer("Thanks for Playing!")
            time.sleep(1)
            sys.exit()
        else:
            # Invalid Input Filtering
            print("Invalid Input, Try Again")
