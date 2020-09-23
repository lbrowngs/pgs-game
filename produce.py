# these first lines should be taken care of by a different file I think
from confidence import confidence
from personTest import person
player = person("Tom")
name = player.sayName()
conf = confidence(name)

#PRODUCE AISLE

#MASK PROTESTOR SCENARIO
#should write a variable of whether they saw flour man or not?
print(f"{name} heads over to grab some bananas.  Upon reaching the isle, {name} sees the flour-hoarding man now with his mask completely off in a shouting match with an employee. This man is now waving a fake looking document shouting that he does not need a mask!")
protestChoice = input("What should they do? A: Join the man's protest B: Stick up for the employee C: Grab bananas and run away.")
protestChoice = protestChoice.upper()



