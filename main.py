import sys
from confidence import confidence

name = input("Welcome to PGS! Pandemic Grocery Shopping! \nWhat is your name?")
conf = confidence(name)

print(f"Our story begins with our hero {name} who has been stuck at home for 6 months \nand really wants to bake an amazing banana bread. Is {name} ready to dodge potential carriers \nwhile getting what they needs to make this tasty treat? Will {name} over come they anxiety \nand fear for the mouthwatering bread stuffed with bananas? Let’s find out!")

continueChoice = input("Shall we continue? \nA: Yes \nB: No \nAnswer: ")
continueChoice = continueChoice.upper()

if continueChoice == "A":
    print("You have chosen wisely, go face your fears!")
elif continueChoice == "B":
    print("You have chosen tasteless death. No tasty bread for you, stay home!")
    sys.exit()

#item selection
