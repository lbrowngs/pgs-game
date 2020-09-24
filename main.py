import sys
from confidence import confidence
from baking import baking

name = input("Welcome to PGS! Pandemic Grocery Shopping! \nWhat is your name?")
conf = confidence(name)

print(f"Our story begins with our hero {name} who has been stuck at home for 6 months \nand really wants to bake an amazing banana bread. Is {name} ready to dodge potential carriers \nwhile getting what they needs to make this tasty treat? Will {name} over come they anxiety \nand fear for the mouthwatering bread stuffed with bananas? Let’s find out!")

continueChoice = input("Shall we continue? \nA: Yes \nB: No \nAnswer: ")
continueChoice = continueChoice.upper()

if continueChoice == "A":
    print(f"{name} has chosen wisely, go face the fear!")
elif continueChoice == "B":
    print(f"{name} has chosen tasteless death. No tasty bread for {name}, stay home!")
    sys.exit()

#item selection

#baking aisle
bakedGoods = baking(name)
bakedGoods.bakingAisle()


