# these first lines should be taken care of by a different file I think
from confidence import confidence

# Canned Goods AISLE

class canned():
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

    def cannedAisle(self):
        name = self.name
        conf = self.confidence

        # canned stocking scenario
        print(f"\n{name} stands at the entrance to the canned goods aisle. There's nothing on the grocery list to get from this aisle, but they can enter if they wish.")
        enter = input(f"\nShould {name} enter the aisle? \nA: Yes \nB: No")
        enter = enter.upper()
        if enter == "A":
            input(f"test")
        elif enter == "B":
            print(f"\n{name} does not enter.")

