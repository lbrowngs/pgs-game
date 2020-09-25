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
        print(f"\nUpon entering the aisle, {name} comes across a staff member with a towering stocking cart. The staff member is stocking some canned tomatoes, and she and the cart take up a good amount of space in the narrow aisle. {name} needs to get past her.")
        run_or_alert = input(f"\nShould they rush past or politely alert the staff? \nA: run past \nB: politely alert the staff \nAnswer:" )
        run_or_alert = run_or_alert.upper()
        if run_or_alert == "A":
            print(f"\n{name} attempts to quickly move past the employee, but they don’t see a stocking box on the floor in their path. They trip, falling toward the staff member and in the process ripping her mask off. A manager rounds the corner and immediately kicks {name} out of the store, despite their apologies. ")
            conf.change(-20)
        elif run_or_alert == "B":
            print(f"\n{name} clears their throat and says “excuse me” to the staff member, who looks up, smiles, and moves to the edge of the aisle to let {name} safely pass by. {name} carefully steps over a box on the floor, avoiding potential disaster. As {name} is walking away, they hear the staff member say “Wait!” and turn around. The staff member, still smiling, holds out a can labeled 'special ingredient', and asks if {name} would like them. They gratefully accept and both move on. ")
            print(f"\nNow {name} has a special ingredient! {name} heads to another aisle. ")





