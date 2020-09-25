from confidence import confidence
from gameover import gameEnd

#CHECKOUT
class checkout():

    def __init__(self, name, confidence, item, special):
        self.name = name
        self.confidence = confidence
        self.item = item
        self.special = special

    def check_out(self):
        name = self.name
        conf = self.confidence
        item = self.item
        special_item = self.special
    
        #CHECKOUT SCENARIO
        input(f"\n{name} enters the checkout line. ")
        input(f"When it’s their turn, the checker informs them that they can use their own bags, \nbut only if they bag their items. ")
        input(f"Otherwise, the checker can bag the items for them in paper store bags.")
        bagChoice = input("\nWhat should they do? \nA: Use their own bags \nB: Use the store-provided paper bags \nAnswer: ")
        bagChoice = bagChoice.upper() 

        while bagChoice not in ["A", "B"]:
            bagChoice = input("\nPlease make a selection, A or B.: ")
            bagChoice = bagChoice.upper()

        if bagChoice == "A":
            input(f"\n{name} decides to use their own reusable bags, \nand starts bagging as soon as each item is scanned by the cashier.")
            input(f"But the cashier starts scanning faster and faster, and {name} can’t quite keep up with the speed.")
            input(f"The person waiting in line behind them is staring impatiently.")
            speedChoice = input(f"\nShould {name} speed up their bagging? \nA: Yes \nB: No \nAnswer: ")
            speedChoice = speedChoice.upper()

            while speedChoice not in ["A", "B"]:
                speedChoice = input("\nPlease make a selection, A or B.")
                speedChoice = speedChoice.upper()

            if speedChoice == "A":
                input(f"\n{name} nervously and quickly bags the rest of their items, but squishes one of the bananas in the process!")
                conf.change(-1)
            elif speedChoice == "B":
                input(f"\n{name} wants to keep bagging at the same speed and ignore the impatient cashier and customer. \nThis will require 8 confidence – do they have enough?")
                confVal = conf.return_int()
                print(f"Confidence level is {confVal}")

                if confVal >= 8:
                    input(f"\n{name} feels so confident, they can ignore the impatient glances. \nThey keep bagging at the same speed and protect the bananas from being squashed by the flour.")

                elif confVal < 8:
                    input(f"\n{name} doesn't have enough confidence.")
                    picChoice = input(f"\nBut their item might help, should they look at a picture of their dog? \nA: Yes \nB: No \nAnswer: ")
                    picChoice = picChoice.upper()

                    while picChoice not in ["A", "B"]:
                        picChoice = input("\nPlease make a selection, A or B.")
                        picChoice = picChoice.upper()

                    if picChoice == "A":
                        if item == "picture of dog":
                           input(f"\n{name} looks at a picture of their adorable dog, their loyal companion, and feels a boost of confidence.")
                           conf.change(6)
                           newConf = conf.return_int()
                           if newConf >=8:
                               input(f"\n{name} feels so confident, they can ignore the impatient glances. \nThey keep bagging at the same speed and protect the bananas from being squashed by the flour.")
                           elif newConf < 8:
                               input(f"\nWithout enough confidence to face the impatient people around them, {name} speeds up bagging, but squishes a banana in the process!")
                               conf.change(-1)
                        else:
                            input(f"\n{name} doesn't have a picture of their dog!")
                            input(f"\nWithout enough confidence to face the impatient people around them, {name} speeds up bagging, but squishes a banana in the process!")
                            conf.change(-1)
                    
                    elif picChoice == "B":
                        input(f"\nWithout enough confidence to face the impatient people around them, {name} speeds up bagging, but squishes a banana in the process!")
                        conf.change(-1)



        elif bagChoice == "B":
            input(f"\n{name} lets the cashier bag their items and opts for the paper bags from the store.")
        
        
        #CHECK FOR SPECIAL ITEM
        game = gameEnd(name)

        if special_item == "special":
            print("special item!! yay!!")
            #call special win from gameover
        else:
            input(f"The cashier finishes ringing up the items, and {name} pays and heads home. \n")
            game.win()
