# NZ Motorsport Quiz

import time
import sys

# Quiz Dictionary
quiznz = {
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

quizau = {
    1: {
        "question": "Who is the only driver to win the Formula One World Championship in a car bearing their own name?",
        "options": "A. Alan Jones, B. Jack Brabham, C. Mark Webber, D. Peter Brock",
        "answer": "B"
    },
    2: {
        "question": "How many Formula One World Drivers' Championships did Jack Brabham win?",
        "options": "A. 1, B. 2, C. 3, D. 4",
        "answer": "C"
    },
    3: {
        "question": "Which Australian driver won the Formula One World Championship for Williams in 1980?",
        "options": "A. Mark Webber, B. Alan Jones, C. David Brabham, D. Daniel Ricciardo",
        "answer": "B"
    },
    4: {
        "question": "True or False: Mark Webber finished on the podium in the Formula One Drivers’ Championship three times.",
        "options": "A. True, B. False",
        "answer": "A"
    },
    5: {
        "question": "How many MotoGP World Championships did Mick Doohan win?",
        "options": "A. 3, B. 4, C. 5, D. 6",
        "answer": "C"
    },
    6: {
        "question": "Which Australian won the Bathurst 1000 a record nine times?",
        "options": "A. Peter Brock, B. Craig Lowndes, C. Jamie Whincup, D. Allan Moffat",
        "answer": "A"
    },
    7: {
        "question": "Who was the first Australian to win the 24 Hours of Le Mans?",
        "options": "A. Mark Webber, B. Vern Schuppan, C. David Brabham, D. Larry Perkins",
        "answer": "B"
    },
    8: {
        "question": "True or False: Casey Stoner won two MotoGP World Championships.",
        "options": "A. True, B. False",
        "answer": "A"
    },
    9: {
        "question": "Who is the only Australian to lead the F1 Championship since 2014?",
        "options": "A. Oscar Piastri, B. Daniel Ricciardo, C. Jack Doohan, D. Mark Webber",
        "answer": "A"
    },
    10: {
        "question": "Which Australian driver finished second at the 2015 24 Hours of Le Mans?",
        "options": "A. Mark Webber, B. David Brabham, C. Will Power, D. Jamie Whincup",
        "answer": "A"
    },
    11: {
        "question": "How many Grand Prix victories did Mark Webber achieve in Formula 1?",
        "options": "A. 5, B. 7, C. 9, D. 11",
        "answer": "C"
    },
    12: {
        "question": "Who was the first Australian to win the Formula One World Drivers' Championship?",
        "options": "A. Alan Jones, B. Jack Brabham, C. Mark Webber, D. Peter Brock",
        "answer": "B"
    },
    13: {
        "question": "Which Australian motorcycle racer was elevated to Legend status in the Australian Motorsport Hall of Fame in 2025?",
        "options": "A. Mick Doohan, B. Casey Stoner, C. Wayne Gardner, D. Troy Bayliss",
        "answer": "B"
    },
    14: {
        "question": "True or False: Peter Brock won the Australian Touring Car Championship more than any other driver.",
        "options": "A. True, B. False",
        "answer": "B"
    },
    15: {
        "question": "Which Australian driver won the 2014 Indianapolis 500?",
        "options": "A. Will Power, B. Scott Dixon, C. James Courtney, D. David Brabham",
        "answer": "A"
    },
    16: {
        "question": "How many Bathurst 1000's did Mark Skaife win?",
        "options": "A. 5, B. 6, C. 7, D. 8",
        "answer": "B"
    },
    17: {
        "question": "Who was the first Australian to win a Formula One Grand Prix?",
        "options": "A. Jack Brabham, B. Alan Jones, C. Mark Webber, D. Tim Schenken",
        "answer": "A"
    },
    18: {
        "question": "Which Australian driver has won the most V8 Supercars championships?",
        "options": "A. Peter Brock, B. Jamie Whincup, C. Craig Lowndes, D. Mark Skaife",
        "answer": "B"
    },
    19: {
        "question": "True or False: James Courtney is a member of the Australian Motorsport Hall of Fame.",
        "options": "A. True, B. False",
        "answer": "A"
    },
    20: {
        "question": "Which Australian driver co-founded the Brabham Formula One team?",
        "options": "A. Alan Jones, B. Mark Webber, C. Jack Brabham, D. David Brabham",
        "answer": "C"
    }
}

quizuk = {
    1: {
        "question": "Who holds the record for the most Formula 1 World Championships for the United Kingdom?",
        "options": "A. Jackie Stewart, B. Lewis Hamilton, C. Jenson Button, D. Damon Hill",
        "answer": "B"
    },
    2: {
        "question": "How many World Drivers' Championships has Lewis Hamilton won?",
        "options": "A. 5, B. 6, C. 7, D. 8",
        "answer": "C"
    },
    3: {
        "question": "Which British driver won the F1 World Championship in 1992?",
        "options": "A. Nigel Mansell, B. Damon Hill, C. Jenson Button, D. Graham Hill",
        "answer": "A"
    },
    4: {
        "question": "True or False: Jenson Button won his F1 title with McLaren.",
        "options": "A. True, B. False",
        "answer": "B"
    },
    5: {
        "question": "Which British driver is the only person to win world championships on both two and four wheels?",
        "options": "A. John Surtees, B. Jim Clark, C. Mike Hawthorn, D. James Hunt",
        "answer": "A"
    },
    6: {
        "question": "How many British drivers have won the F1 World Championship?",
        "options": "A. 7, B. 8, C. 9, D. 10",
        "answer": "D"
    },
    7: {
        "question": "Who was the first British driver to win the F1 World Championship?",
        "options": "A. Mike Hawthorn, B. Graham Hill, C. Jim Clark, D. Jackie Stewart",
        "answer": "A"
    },
    8: {
        "question": "Which British driver won the F1 World Championship in 1976?",
        "options": "A. James Hunt, B. Jackie Stewart, C. Nigel Mansell, D. Damon Hill",
        "answer": "A"
    },
    9: {
        "question": "Who won the F1 World Championship for Williams in 1996?",
        "options": "A. Damon Hill, B. Nigel Mansell, C. Jenson Button, D. Lewis Hamilton",
        "answer": "A"
    },
    10: {
        "question": "True or False: Graham Hill is the only driver to win the Triple Crown of Motorsport (Monaco GP, Le Mans, Indy 500).",
        "options": "A. True, B. False",
        "answer": "A"
    }
}

quizde = {
    1: {
        "question": "Which German driver holds the record for the most Formula 1 World Championships?",
        "options": "A. Sebastian Vettel, B. Michael Schumacher, C. Nico Rosberg, D. Ralf Schumacher",
        "answer": "B"
    },
    2: {
        "question": "How many F1 World Championships did Michael Schumacher win?",
        "options": "A. 5, B. 6, C. 7, D. 8",
        "answer": "C"
    },
    3: {
        "question": "Which German driver won four consecutive F1 World Championships from 2010 to 2013?",
        "options": "A. Michael Schumacher, B. Sebastian Vettel, C. Nico Rosberg, D. Nick Heidfeld",
        "answer": "B"
    },
    4: {
        "question": "True or False: Nico Rosberg won his only F1 World Championship in 2016.",
        "options": "A. True, B. False",
        "answer": "A"
    },
    5: {
        "question": "How many points did Michael Schumacher score all time?",
        "options": "A. 500-750, B. 750-1000, C. 1000-1500, D. 1500+",
        "answer": "D"
    },
    6: {
        "question": "How many German drivers have won the F1 World Championship?",
        "options": "A. 2, B. 3, C. 4, D. 5",
        "answer": "B"
    },
    7: {
        "question": "Which German team has the most F1 Constructors’ Championships?",
        "options": "A. Mercedes, B. BMW, C. Porsche, D. Audi",
        "answer": "A"
    },
    8: {
        "question": "Who was the first German to win the F1 World Championship?",
        "options": "A. Michael Schumacher, B. Sebastian Vettel, C. Nico Rosberg, D. None",
        "answer": "A"
    },
    9: {
        "question": "True or False: Sebastian Vettel won a title with Ferrari.",
        "options": "A. True, B. False",
        "answer": "B"
    },
    10: {
        "question": "Which German driver retired immediately after winning his only F1 World Championship?",
        "options": "A. Keke Rosberg, B. Sebastian Vettel, C. Nico Rosberg, D. Heinz-Harald Frentzen",
        "answer": "C"
    }
}

quizbr = {
    1: {
        "question": "Who is the only Brazilian driver to win three Formula 1 World Championships?",
        "options": "A. Ayrton Senna, B. Nelson Piquet, C. Emerson Fittipaldi, D. Rubens Barrichello",
        "answer": "A"
    },
    2: {
        "question": "How many F1 World Championships did Emerson Fittipaldi win?",
        "options": "A. 1, B. 2, C. 3, D. 4",
        "answer": "B"
    },
    3: {
        "question": "Which Brazilian driver was the first to win the F1 World Championship?",
        "options": "A. Ayrton Senna, B. Nelson Piquet, C. Emerson Fittipaldi, D. Felipe Massa",
        "answer": "C"
    },
    4: {
        "question": "True or False: Rubens Barrichello won an F1 World Championship.",
        "options": "A. True, B. False",
        "answer": "B"
    },
    5: {
        "question": "How many World Championships did Ayrton Senna win?",
        "options": "A. 2, B. 3, C. 4, D. 5",
        "answer": "B"
    },
    6: {
        "question": "Which Brazilian driver won the F1 World Championship in 1981, 1983, and 1987?",
        "options": "A. Ayrton Senna, B. Nelson Piquet, C. Emerson Fittipaldi, D. Felipe Massa",
        "answer": "B"
    },
    7: {
        "question": "Who was the last Brazilian to win the F1 World Championship?",
        "options": "A. Ayrton Senna, B. Nelson Piquet, C. Emerson Fittipaldi, D. Felipe Massa",
        "answer": "A"
    },
    8: {
        "question": "Which Brazilian driver won the F1 World Championship in 1972 and 1974?",
        "options": "A. Ayrton Senna, B. Nelson Piquet, C. Emerson Fittipaldi, D. Rubens Barrichello",
        "answer": "C"
    },
    9: {
        "question": "True or False: Felipe Massa won the F1 World Championship in 2008.",
        "options": "A. True, B. False",
        "answer": "B"
    },
    10: {
        "question": "How many Brazilian drivers have won the F1 World Championship?",
        "options": "A. 2, B. 3, C. 4, D. 5",
        "answer": "B"
    }
}

quiz_map = {
    "A": quiznz,
    "B": quizau,
    "C": quizuk,
    "D": quizde,
    "E": quizbr
}

def quizpicker():
    while True:
        option = input("Select a country:\n"
                    "A. New Zealand\n"
                    "B. Australia\n"
                    "C. United Kingdom\n"
                    "D. Germany\n"
                    "E. Brazil\n"
                    "Enter your choice (A-E): ").upper()
        if option in quiz_map:
            return quiz_map[option]
            break
        else:
            print("Invalid Input, Try Again")

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
welcomer("Welcome to Motorsport Quizzes! Pick a country to get quizzed on their drivers!")
time.sleep(0.375)
quizpicker
quizname = quizpicker()
time.sleep(0.375)
welcomer("Answer using just the letter of each option.")
time.sleep(0.1875)
welcomer("Good Luck!")
print("--------------------")

while True:
    # Reset the score
    score = 0
    # Loop through dictionary in order
    for q_num in quizname:
        # Gets the current question
        q = quizname[q_num]
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
    welcomer(f"Quiz Complete, Well Done! You scored: {score} out of {len(quizname)}")
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
            quizpicker
            quizname = quizpicker()
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
