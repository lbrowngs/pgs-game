import sys
from art import *

gameOverArt = text2art("Game Over!")
gameWinArt = text2art("For The Win!")

class gameOver():

    def over(self):
        print(f"{name} is back at home without the ingredients to make the amazing banana bread. What a sad day it is!")
        print(gameOverArt)
        sys.exit()

class gameWin():
    
    def win(self):
        print(f"{name} is back at home enjoying the amazing banana bread! What a glorious day it is!")
        print(gameWinArt)
        sys.exit()