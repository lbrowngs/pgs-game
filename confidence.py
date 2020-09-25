from gameover import gameEnd

class confidence():

    def __init__(self, name):
        self.value = 10
        self.name = name

    def return_int(self):
        return self.value
    
    def show(self):
        print("Confidence is " + str(self.value))

    def change(self, change):
        val = self.value + change
        self.value = val

        if (self.value > 0):
            if (change > 0):
                print("Confidence has increased by " + str(change))
            elif (change < 0):
                change = abs(change)
                print("Confidence has decreased by " + str(change))

            print("Confidence is now " + str(self.value))

        if (self.value == 1):
            print("Confidence level is one! Be careful!")

        if (self.value <= 0):
            print(f"Confidence has dropped to zero and {self.name} can no longer handle the stresses of grocery shopping. {self.name} runs out of the store, leaving all items behind.")
            game = gameEnd(self.name)
            game.over()
