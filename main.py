import sys
from confidence import confidence
from baking import baking
from produce import produce
from canned import canned

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
        userItem = input("\nA: hand-sanitizer \nB: picture of dog \nC: headphones \nAnswer: ")
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

#entrance of Covway
print(f"\nLet's head to the grocery store! {name} takes the trusty {specialItem} and gets in the car. {name} takes a deep breath before starting the car and heading to Covway grocery store.  \n")
print(f"{name} has arrived at Covway, as they head to the entrance, there is a hand-sanitizer station with an employee beside it. ")

def handSan():
    while True:
        userAns = input(f"\nChoose what {name} should do: \nA. Use hand-sanitizer station? \nB. Use own hand-sanitizer in front of the employee? \nC. Do nothing, walk by fast to avoid the employee. ")
        userAns = userAns.upper()
        if userAns == "A":
            n = print(f"\nEmployee thanks {name} for using the hand-sanitizer. +1 confidence")
            conf.change(+1)
            break
        elif userAns == "B":
            n = "hand-sanitizer"
            if n == specialItem:
                print(f"\nEmployee thanks {name} for using own hand-sanitizer. +3 confidence")
                conf.change(+2)
                break
            elif n != specialItem:
                print(f"\n{name} does not have this item, choose again!")
                userAns
        elif userAns == "C":
            n = print(f"Employee's eyes frown and stare at {name} as {name} runs by. -2 confidence")
            conf.change(-2)
            break
    return n
print(handSan())

#choosing aisle
available_aisles = set(["baking", "canned", "produce", "frozen"])
aisles_visited = set([])
while available_aisles != aisles_visited:
    aisles = input(f"\nChoose which aisle {name} should go next: \nA. Baking Aisle \nB. Produce Aisle \nC. Canned Goods Aisle \nD. Frozen Aisle \nE. Check-out \nAnswer: ")
    aisles = aisles.upper()
    if aisles == "A":
        # baking aisle
        bakedGoods = baking(name, conf)
        bakedGoods.bakingAisle()
        aisles_visited.add("baking")
    elif aisles == "B":
        # produce aisle
        produceSection = produce(name, conf)
        produceSection.produceAisle()
        aisles_visited.add("produce")
    elif aisles == "C":
        # canned goods
        print("test")
        aisles_visited.add("canned")
    elif aisles == "D":
        print("test")
    elif aisles =="E":
        print("test")




