'''
Project: Rock Paper and Scissor
Ver: 1.0.0
Developer: Abisheek Kumar
Country: India

'''

from asciiArt import getASCIIArt
import random

class RockPaperScissor:
    def __init__(self):
        self.options = ["rock","paper","scissor"]

    def computerChoice(self):
        computerSelection = random.choice(self.options)
        return computerSelection
        
    def userChoice(self,usrInput):
        return self.options[usrInput]
            
    def validateResult(self,usrChoice,compChoice):
        try:
            win_against = {
                "rock":"scissor",
                "scissor":"paper",
                "paper":"rock"
            }
            if usrChoice == compChoice:
                return None
            return win_against[usrChoice] == compChoice
        except Exception as validationError:
            print(f"Error in validating the result: {validationError}")

    def startGame(self):
        try:
            usrInput = int(input("Enter your choice 0 for rock, 1 for paper or 2 for scissor:\n"))
            if usrInput >=0 and usrInput <=2:
                usrChoice = self.userChoice(usrInput) 
                print(f"Your choice: {usrChoice.capitalize()}\n")
                getASCIIArt(usrChoice)
                compChoice = self.computerChoice()
                print(f"Computer's choice: {compChoice.capitalize()}\n")
                getASCIIArt(compChoice)
                result = self.validateResult(usrChoice,compChoice)
                if type(result) == bool:
                    return "You win!" if result else "You lose!"
                else:
                    return "Game draw"
            else:
                return "Invalid input! only 0,1 or 2 can be given!"
                
        except Exception as gameError:
            print(f"Error in gameplay: {gameError}")

finalRes = RockPaperScissor()
res = finalRes.startGame()
print(res)