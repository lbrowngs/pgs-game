import sys
from art import *

gameOverArt = text2art("Game Over!")
gameWinArt = text2art("You Win!")

class gameOver():

    def over(self):
        print("You are back in your home without the ingredients to make the amazing banana bread.")
        print(gameOverArt)
        sys.exit()

class gameWin():
    
    def win(self):
        print("You are back at home enjoying your amazing banana bread!")
        print(gameWinArt)
        sys.exit()