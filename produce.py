# these first lines should be taken care of by a different file I think
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
        print(f"{name} heads over to grab some bananas.  Upon reaching the isle, {name} sees the flour-hoarding man now with his mask completely off in a shouting match with an employee. This man is now waving a fake looking document shouting that he does not need a mask!")
        protestChoice = input("What should they do? \nA: Join the man's protest \nB: Stick up for the employee \nC: Grab bananas and run away. \nAnswer: ")
        protestChoice = protestChoice.upper()
        
        



