# these first lines should be taken care of by a different file I think
from confidence import confidence

# Frozen AISLE

class frozen():
    def __init__(self, name, confidence, item, special):
        self.name = name
        self.confidence = confidence
        self.item = item
        self.special = special

    def frozen_aisle(self):
        name = self.name
        conf = self.confidence
        item = self.item
        special_item = self.special

        # frozen scenario
        print(f"\n{name} arrives to the frozen section and hears loud yelling. {name} notices a man in a red hat shouting “5G is killing our kids!”.  Upon further observation {name} realizes it is the same flour hoarding, documenting faking, loud man from the previous aisles. ")
        red_hat = input(f"\nWhat should {name} do? \nA: user headphones? \nB: confront him again! \nC: call the employees again so they can deal with him. \nD: leave aisle")
        red_hat = red_hat.upper()
        if red_hat == "A":
            


