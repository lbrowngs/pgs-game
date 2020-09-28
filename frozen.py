# these first lines should be taken care of by a different file I think
from confidence import confidence

# Frozen AISLE

class frozen():
    def __init__(self, name, confidence, item):
        self.name = name
        self.confidence = confidence
        self.item = item


    def frozen_aisle(self):
        name = self.name
        conf = self.confidence
        item = self.item

        # frozen scenario
        print(f"\n{name} arrives to the frozen section and hears loud yelling. {name} notices a man in a red hat shouting “5G is killing our kids!”.  Upon further observation {name} realizes it is the same flour hoarding, documenting faking, loud man from the previous aisles. ")
        red_hat = input(f"\nWhat should {name} do? \nA: user headphones? \nB: confront him again! \nC: call the employees again so they can deal with him. \nD: leave aisle \nAnswer: ")
        red_hat = red_hat.upper()
        if red_hat == "A" and item == "headphones":
            print(f"{name} puts on the headphones and ignores the red hat man, avoiding the situation all together. Confidence has not changed.")
        elif red_hat == "A" and item != "headphones":
            print(f"{name} does not have, choose something else!")
            red_hat
        elif red_hat == "B":
            print(f"{name} is brave but not smart, Red Hat Man spits as he yells at {name} causing a potential Covid spreading situation. Both him and {name} get kicked out of the store.")
            conf.change(-20)
        elif red_hat == "C":
            print(f"{name} calls the employees again to deal with this horrible man. Confidence decreases by -1.")
        elif red_hat == "D":
            print(f"{name} leaves the aisle with nothing. Confidence decreases by -3.")
            conf.change(-3)
        



            


