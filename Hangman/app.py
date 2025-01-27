# import random
# from icons import icons

# class Hangman:
#     def __init__(self):
#         self.words = ["BHARATH","SANGEETH","GHAJAR","FLUTE","MRIDANGA"]
#         self.appreciations = ["Wow! Great","Kudos! you guessed it.","Good,you got it!","Awesome!"]
#         self.actualWord = random.choice(self.words)
#         self.blanks = "_" * len(self.words)
#         self.n = len(self.words)
#         self.lifeStatus = len(self.words)
        
#     def getLetter(self,letter):
#         try:
#             print(f"FSDLJFKJNKJNBKJBNFG: {self.actualWord}")
#             upperCase = letter.upper()
#             print(f"You have entered: {upperCase}")
#             if upperCase in self.actualWord:
#                 index = self.actualWord.index(upperCase)
#                 blank1 = list(self.blanks)
#                 blank1[index] = upperCase
#                 self.blanks = ''.join(blank1)
#                 print(random.choice(self.appreciations))
#                 self.n -= 1
#             else:
#                 print("Oh,oh! you lost one life. Try again!")
#                 self.lifeStatus -= 1
            
#         except Exception as letterError:
#             print(f"Error in getting the word: {letterError}")
    
#     def startGame(self):
#         try:
#             print(icons["welcome"])
#             while self.n > 0 and self.lifeStatus > 0:
#                 usrInput = input("Enter the letter to guess:")
#                 self.getLetter(usrInput)
#             if self.n == 0:
#                 print("Congratulations! you win 🏆")
#             elif self.lifeStatus == 0:
#                 print("OOPS! The man was hanged.🪢💀")
#         except Exception as startError:
#             print(f"Error in starting the game: {startError}")
            
            
# result = Hangman()
# result.startGame()

import random
from data import wordList

chosen_word = random.choice(wordList)
print(f"Chosen Word: {chosen_word}")

gameover = False
life = 6
visited = []

while not gameover:
    user_choice = input("Enter the letter:").lower()
    display = ""
    for letter in chosen_word:
        if letter == user_choice:
            display += letter
            visited.append(user_choice)
        elif letter in visited:
            display += letter
        else:
            display += "_"
    print(display)
    
    if letter not in chosen_word:
        life -= 1
        if life == 0:
            gameover = True
            print("Oops! you lose.")
    
    if "_" not in display:
        gameover = True
        print("You win!")




    