import sys
from confidence import confidence
from baking import baking
from produce import produce

name = input("Welcome to PGS! Pandemic Grocery Shopping! \nWhat is your name?")
conf = confidence(name)

print(f"\nOur story begins with our hero {name} who has been stuck at home for 6 months \nand really wants to bake an amazing banana bread. Is {name} ready to dodge potential carriers \nwhile getting what they needs to make this tasty treat? Will {name} over come they anxiety \nand fear for the mouthwatering bread stuffed with bananas? Let’s find out!")

continueChoice = input("\nShall we continue? \nA: Yes \nB: No \nAnswer: ")
continueChoice = continueChoice.upper()

if continueChoice == "A":
    input(f"\n{name} has chosen wisely, go face the fear of PGS!")
elif continueChoice == "B":
    print(f"\n{name} has chosen tasteless death. No tasty bread for {name}, stay home!")
    sys.exit()

#item selection
print(f"\nBefore {name} goes, here are some items {name} can take.  Choose only 1 item to assist {name} in his journey to delicious banana bread glory.")

def item():
    while True:
        userItem = input("\nA: hand-sanitizer \nB: picture of dog \nC: headphones \nAnswer:")
        userItem = userItem.upper()
        if userItem == "A":
            x = "hand-sanitizer"
            break
        elif userItem == "B":
            x = "picture of dog"
            break
        elif userItem == "C":
            x = "headphones"
            break
    return x
specialItem = item()

print(specialItem)

#baking aisle
# bakedGoods = baking(name, conf)
# bakedGoods.bakingAisle()

#produce aisle - temp
# produceSection = produce(name, conf)
# produceSection.produceAisle()


