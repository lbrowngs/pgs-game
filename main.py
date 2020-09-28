import sys
from confidence import confidence
from baking import baking
from produce import produce
from canned import canned
from frozen import frozen
from checkout import checkout

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
            n = print(f"\nEmployee thanks {name} for using the hand-sanitizer. Confidence has increased by +1")
            conf.change(+1)
            break
        elif userAns == "B":
            n = "hand-sanitizer"
            if n == specialItem:
                print(f"\nEmployee thanks {name} for using own hand-sanitizer. Confidence has increased by +3")
                conf.change(+3)
                break
            elif n != specialItem:
                print(f"\n{name} does not have this item, choose again!")
                userAns
        elif userAns == "C":
            n = print(f"Employee's eyes frown and stare at {name} as {name} runs by. Confidence has decreased by -2")
            conf.change(-2)
            break
    return n
handSan()

#choosing aisle
available_aisles = set(["A. Baking", "B. Produce", "C. Canned Goods", "D. Frozen"])
aisles_visited = set([])
while available_aisles != aisles_visited:
    not_visited = sorted(list(available_aisles.difference(aisles_visited)))
    aisles_left = '\n'.join(not_visited)
    aisles = input(f"\nChoose which aisle {name} should go next: \n{aisles_left} \nAnswer: ")
    aisles = aisles.upper()
    if aisles == "A":
        # baking aisle
        bakedGoods = baking(name, conf)
        bakedGoods.bakingAisle()
        aisles_visited.add("A. Baking")
    elif aisles == "B":
        # produce aisle
        produceSection = produce(name, conf)
        produceSection.produceAisle()
        aisles_visited.add("B. Produce")
    elif aisles == "C":
        # canned goods
        print(f"\n{name} stands at the entrance to the canned goods aisle. There's nothing on the grocery list to get from this aisle, but they can enter if they wish.")
        enter = input(f"\nShould {name} enter the aisle? \nA: Yes \nB: No \nAnswer: ")
        enter = enter.upper()
        if enter == "A":
            cannedGoods = canned(name, conf)
            cannedGoods.cannedAisle()
            aisles_visited.add("C. Canned Goods")
            special_ingredient = "special"
        elif enter == "B":
            print(f"\n{name} turns away, the shimmering, well-organized aisle of cans upon cans now behind them.")
            special_ingredient = "none"
            aisles_visited.add("C. Canned Goods")
    elif aisles == "D":
        frozenSection = frozen(name, conf, specialItem)
        frozenSection.frozen_aisle()
        aisles_visited.add("D. Frozen")

input(f"{name} has gathered all items needed and can now head to checkout.")
checkOut = checkout(name, conf, specialItem, special_ingredient)
checkOut.check_out()




