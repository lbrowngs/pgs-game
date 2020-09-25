from confidence import confidence

#PRODUCE AISLE
class produce():
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

    def produceAisle(self):
        name = self.name
        conf = self.confidence

        #MASK PROTESTOR SCENARIO
        #should write a variable of whether they saw flour man or not?
        input(f"\n{name} heads over to grab some bananas.  \nUpon reaching the aisle, {name} sees the flour-hoarding man now with his mask completely off, \nin a shouting match with an employee." )
        input(f"This man is waving a fake looking document shouting that he does not need a mask! ")
        protestChoice = input("\nWhat should they do? \nA: Join the man's protest \nB: Stick up for the employee \nC: Grab bananas and run away. \nAnswer: ")
        protestChoice = protestChoice.upper()

        while protestChoice not in ["A", "B", "C"]:
            protestChoice = input("\nPlease make a selection, A, B, or C.: ")
            protestChoice = protestChoice.upper()

        if protestChoice == "A":
            input(f"\n{name} decides they are fed up and they, too, don't care about the health of others. \nThey join in protesting with the man. \nThe store employee is not pleased with this, and asks both the man and {name} to leave. ")
            conf.change(-10)
        elif protestChoice == "B":
            input(f"\n{name} steps in between the shouting man and the employee, and tells the man they don't care about any fake legal document, they need to wear a mask! \nThe employee is clearly relieved, and thanks {name} as security escorts the man out of the store.")
            conf.change(2)
        elif protestChoice == "C":
            input(f"\n{name} doesn't want to deal with this drama. \nThey sneak behind the shouting man and grab a bunch of bananas. \nAs they walk away, they hear the employee burst into tears.")
            conf.change(-2)

        input(f"\n{name} continues down the produce aisle, and encounters a sample station.")
        input(f"The samples are fresh slices of juicy watermelon.")
        sampleChoice = input("\nWhere should they take their sample to try it out? \nA: Nowhere, just eat it right there! \nB: Away from the sample station. \nAnswer: ")
        sampleChoice = sampleChoice.upper()

        while sampleChoice not in ["A", "B"]:
            sampleChoice = input("\nPlease make a selection, A or B.: ")
            sampleChoice = sampleChoice.upper()

        if sampleChoice == "A":
            input(f"\nAs {name} cruches down on the fresh watermelon, the employee serving samples glares. \nThey angrily remind {name} to not remove their mask while standing close to others, even to eat.")
            conf.change(-2)
        elif sampleChoice == "B":
            input(f"\n{name} steps away from the sample station and to an emptier part of the store, and quietly enjoys a delicious slice of watermelon.")
            conf.change(1)

        input(f"\n{name} now has bananas, and can head to a different aisle.")
        




