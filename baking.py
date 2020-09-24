# these first lines should be taken care of by a different file I think
from confidence import confidence
from personTest import person
player = person("Tom")
name = player.sayName()
conf = confidence(name)

# BAKING AISLE

# FLOUR HOARDING SCENARIO
print(f"As {name} heads to the flour section there is a sign that reads '1 bag per customer'. As {name} enters the aisle, {name} is shocked to see it almost completely empty. But behold, tucked in the corner of the middle shelf, is a lone bag of flour.  As {name} goes to grab it, they notice a man, who barely has a mask over his mouth, reaching for the bag. {name} notices this man already has 3 bags of flour in his cart.")
flourChoice = input("What should they do? \nA: Grab the flour bag and run! \nB: Confront the flour hoarder. \nC: Grab the flour bag and alert an employee to the hoarding. \nAnswer: ")
flourChoice = flourChoice.upper()

if flourChoice == "A":
    print(f"{name} deftly dodges the flour hoarder and snatches the last bag of flour, fleeing before the grumpy man can confront them.")
elif flourChoice == "B":
    print(f"{name} turns toward the flour hoarder and points out the sign that says '1 bag per customer.' The man explodes with rage and grabs the last bag of flour from the shelf, throwing it at {name}.")
    conf.change(-10)
elif flourChoice == "C":
    print(f"{name} quickly grabs the last bag of flour and finds an employee further down the aisle. They alert the employee to the flour hoarding situation, and are thanked for their efforts.")
    conf.change(3)


# VANILLA SCENARIO
print(f"{name} now must go grab some very specific vanilla that their S.O. has strictly asked for. As {name} approaches the vast ocean of options, they start to sweat and become nervous in searching for the climate-friendly, Madagascar-conscious, super premium vanilla.")
print(f"{name} starts to search but notices a person behind waiting to get vanilla themselves.")

vanChoice = input("What should they do? A: Grab the first vanilla they see. B: Keep looking and find the vanilla their S.O. asked for. : ")
vanChoice = vanChoice.upper()

if vanChoice == "A":
    print(f"{name} quickly grabs the first vanilla they see, rushing out of the aisle. But they can't stop thinking about their S.O.'s disappointed face.")
    conf.change(-3)
elif vanChoice == "B":
    print(f"{name} continues looking, feeling the long stare of impatience from the person waiting behind them. {name} finally finds the correct vanilla and gets out of the aisle.")
    conf.change(-2)


#DONE WITH BAKING AISLE
print(f"{name} now has both flour and vanilla, and can head to a different aisle.")