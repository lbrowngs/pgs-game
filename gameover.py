import sys
from art import *

gameOverArt = text2art("Game Over!")
gameWinArt = text2art("For The Win!")

class gameEnd():

    def __init__(self, name):
        self.name = name

    def over(self):
        name = self.name
        print(f"{name} is back at home without the ingredients to make the amazing banana bread. What a sad day it is!")
        print(gameOverArt)
        sys.exit()

    def win(self):
        name = self.name
        print(f"{name} is back at home enjoying the amazing banana bread! What a glorious day it is!")
        print(gameWinArt)
        sys.exit()