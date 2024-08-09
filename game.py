print(
    "      QQQQ        U       U    I    ZZZZZZ     ZZZZZZ         GGGG           A         M          M    E E E E E       ")
print(
    "    Q      Q      U       U    I        Z          Z        G      G        A A        M M      M M    E             ")
print(
    "    Q      Q      U       U    I       Z          Z         G              A   A       M     M    M    E            ")
print(
    "    Q      Q      U       U    I      Z          Z          G   GGGG      A A A A      M          M    E E E E E        ")
print(
    "    Q    Q Q      U       U    I     Z          Z           G      G     A       A     M          M    E            ")
print(
    "      QQQQ Q        UUUUU      I    ZZZZZZ     ZZZZZZ         GGGG      A         A    M          M    E E E E E      ")
print(
    "             Q                                                                                                  ")



print("Hello and Welcome to the Quizz GAME!\nThe place where you gonna challenge yourself with some of the general knowledge questions.")
playing = input("Are you ready to play? ")
if playing != "yes":
    quit()
else:
    print("OK, then let's countinue!")
name = input("Please enter your name: ")
if name == "Malvina" or name == "malvina":
    print("Hello my love " + str(name.upper()))
else:
    print("Hello", str(name.upper()))
name_len = len(name)
print("Nice to have you on board!")
print("Did you know your name length is " + str(name_len) + " characters long?")
print("Today we gonna practice some of your knowledge skills.\nAre you Ready? Type Yes or No")
answer = input()


def yes_or_no():
    if answer == "yes" or answer == "Yes":
        print("Let's Continue " + str(name.upper()))
    elif answer == "no" or answer == "No":
        print("Maybe Other Time " + name + "\nSee You SOON!")
        quit()
    else:
        print("Wrong Answer, Please answer with Yes Or No!")


yes_or_no()
    


print("First you need to answer some questions about yourself.")
print("What year you've been born?")
year = int(input())
print("Ok so you are " + str(2024 - year) + " ish old.")
print("What number of the month?")
month = int(input())
print("And what day?")
day = int(input())

from datetime import datetime

now = datetime.now()
birthday = datetime(year, month, day)
print("That means you are " + str(now - birthday))
print("You are completing this steps at " + str(now))

print("With every correct answer given you receive 1 point to your score.")


print("Today we gonna start with 10 simple questions.\nGEOGRAPHY.")

score = 0

#def total_score():





#def total_score():


#question 1
print("What is the longest river in the world?")
answer = input()
if answer.lower() == "nile":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 2
print("What is the biggest ocean on the planet?")
answer = input()
if answer.lower() == "pacific":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 3
print("What is Highest mountain peak in the world?")
answer = input()
if answer.lower() == "everest":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 4
print("What is the largest city in the world by population?")
answer = input()
if answer.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 5
print("What is the biggest island on the planet?")
answer = input()
if answer.lower() == "greenland":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 6
print("What is the capital of Croatia?")
answer = input()
if answer.lower() == "zagreb":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 7
print("And the capital of China?")
answer = input()
if answer.lower() == "beijing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 7
print("What is the biggest desert?")
answer = input()
if answer.lower() == "sahara":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 8
print("What is the capital of Vietnam?")
answer = input()
if answer.lower() == "hanoi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 9
print("What is the largest lake in the world?")
answer = input()
if answer.lower() == "caspian sea":
    print("Correct! It is considered a lake :)")
    score += 1
else:
    print("Incorrect!")

#question 10
print("In wich country we can find Salzburg city?")
answer = input()
if answer.lower() == "austria":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%")

print("TO BE CONTINUE")

