# these first lines should be taken care of by a different file I think
from confidence import confidence

# BAKING AISLE

class baking():
   def __init__(self, name, confidence):
       self.name = name
       self.confidence = confidence
    
   def bakingAisle(self):
        name = self.name
        conf = self.confidence

        # FLOUR HOARDING SCENARIO
        input(f"As {name} heads to the flour section there is a sign that reads '1 bag per customer'. ")
        input(f"{name} enters the aisle and is shocked to see it almost completely empty. \nBut behold, tucked in the corner of the middle shelf, is a lone bag of flour. ")
        input(f"As {name} goes to grab it, they notice a man, who barely has a mask over his mouth, reaching for the bag. \n{name} notices this man already has 3 bags of flour in his cart. ")
        flourChoice = input("\nWhat should they do? \nA: Grab the flour bag and run! \nB: Confront the flour hoarder. \nC: Grab the flour bag and alert an employee to the hoarding. \nAnswer: ")
        flourChoice = flourChoice.upper()

        while flourChoice not in ["A", "B", "C"]:
            flourChoice = input("\nPlease make a selection, A, B, or C.: ")
            flourChoice = flourChoice.upper()

        if flourChoice == "A":
            input(f"\n{name} deftly dodges the flour hoarder and snatches the last bag of flour, fleeing before the grumpy man can confront them. ")
        elif flourChoice == "B":
            input(f"\n{name} turns toward the flour hoarder and points out the sign that says '1 bag per customer.' \nThe man explodes with rage and grabs the last bag of flour from the shelf, throwing it at {name}. ")
            conf.change(-10)
        elif flourChoice == "C":
            input(f"\n{name} quickly grabs the last bag of flour and finds an employee further down the aisle. \nThey alert the employee to the flour hoarding situation, and are thanked for their efforts. ")
            conf.change(3)
            
                



        # VANILLA SCENARIO
        input(f"\n{name} now must go grab some very specific vanilla that their S.O. has strictly asked for. ")
        input(f"As {name} approaches the vast ocean of options, they start to sweat and become nervous in searching for the climate-friendly, Madagascar-conscious, super premium vanilla.")
        input(f"{name} starts to search but notices a person behind waiting to get vanilla themselves.")

        vanChoice = input("\nWhat should they do? \nA: Grab the first vanilla they see. \nB: Keep looking and find the vanilla their S.O. asked for. \nAnswer: ")
        vanChoice = vanChoice.upper()

        while vanChoice not in ["A", "B"]:
            vanChoice = input("\nPlease make a selection, A or B.: ")
            vanChoice = vanChoice.upper()

        if vanChoice == "A":
            input(f"\n{name} quickly grabs the first vanilla they see, rushing out of the aisle. \nBut they can't stop thinking about their S.O.'s disappointed face.")
            conf.change(-3)
        elif vanChoice == "B":
            input(f"\n{name} continues looking, feeling the long stare of impatience from the person waiting behind them. \n{name} finally finds the correct vanilla and gets out of the aisle.")
            conf.change(-2)


        #DONE WITH BAKING AISLE
        input(f"\n{name} now has both flour and vanilla, and can head to a different aisle.")