'''
Project: TREASSURE ISLAND
Version: 1.0.0
Year: 2024
Developer: Abisheek Kumar

'''

from time import sleep
import random
from asciiArt import getASCIIArt

class TreassureIsland:
    def __init__(self):
        self.direction = ["left","right","l","r"]
        self.mode = ["swim","wait",'s','w']
        self.door = ['red','blue','yellow','r','b','y']
        self.treassures = ["Self realization","Mantra Shakthi","Moksha","Powerful weapon","Immortality"]
        self.gods = ["Mahadev","Vishnu","Bhrama","Ganesh","Karthikeya"]

    def printWelcomeMessage(self):
        print("***********************************************************************\n")
        getASCIIArt()
        print("***********************************************************************\n")
        print("Welcome to Island of gods where you can get a precious treassure form them...")
        sleep(3)
        print(" 🙏 But you should have high faith and patience...🙏 you need to pass multiple tests to reach them.")
        sleep(3)
        print(" 🙏 Reaching the precious and permanent treassure is not easy right? Get ready!.")
        sleep(3)
        print("Let's get started...\n")
        sleep(2)

    def selectDoor(self):
        door = input("Which door you want to open? (red,blue,yellow or r,b,y):").lower()
        try:
            if door in self.door:
                if door.startswith('r'):
                    print("OOPS! It's lava over there...🔥🔥🔥 You should ask permission to 'Agni dev' before entering this door")
                    print("Call 'Varun Dev' to save you ⛈️")
                    sleep(2)
                    varun_mantra = input("Type 'Om shri varunaya namah' he will save you:")
                    if varun_mantra == "Om shri varunaya namah":
                        print("Hurray! Varun Dev saved you.. Be careful next time. Come to this island again.")
                        return
                    else:
                        print("Oh! You chanted the mantra wrongly. No issues Agni Dev will forgive you he is always kind.")
                        return
                elif door.startswith('b'):
                    print("OOPS! You got caught by asuras... 👻🧟, Call 'Lord Mahadev🔱' immediately. He will save you!")
                    return
                elif door.startswith('y'):
                    print(" 🎊🎊 CONGRATULATION! YOU GRABBED THE TREASSURE! 🎉🥇💰\n")
                    sleep(1.5)
                    print("Let's see what you got...")
                    sleep(2)
                    print(f" 🙇‍♂️😇 WOW! You got \"{random.choice(self.treassures)}\" from lord {random.choice(self.gods)}...🧘‍♂️🧘‍♂️")
                    return
                else:
                    print("... ❌ Invalid option selected ❌...")
                    return
            else:
                print("Invalid door selected, only (red,blue,yellow or r,b,y) can be opened!")
                return
        except Exception as doorError:
            print(f"Error in selecting the door: {doorError}")
            
    def selectMode(self):
        mode = input("Do you wish to 'swim' or 'wait' for the boat? (swim,wait or s,w):").lower()
        try:
            if mode in self.mode:
                if mode.startswith('w'):
                    print("You boat is near, please wait...")
                    sleep(3)
                    print(" ⛵Your boat has arrived get in quickly....")
                    sleep(3)
                    print("You have three doors to get into the island, 🔴RED | 🔵BLUE | 🟡YELLOW")
                    self.selectDoor()
                elif mode.startswith('s'):
                    print(" 🐊🐊❌⚠️ OOPS! You became the food for crocodiles 🐊🐊❌⚠️, Call 'Lord Vishnu🛞' he will come to save you. ")
                    return
            else:
                print("Invalid mode of transport selected! only (wait,swim or w,s) is allowed")
                return
        except Exception as modeError:
            print(f"Error in selecting the mode of transport to island: {modeError}")
        
    def selectDirection(self):
        direction = input("Which direction you want to go? (left or right):").lower()
        try:
            if direction in self.direction:
                if direction.startswith('l'):
                    print("🏝️ You have reached the lake with island in middle 🏝️\n")
                    self.selectMode()
                elif direction.startswith('r'):
                    print("OOPS! you fell into the hole 🕳️🕳️, say 'hello👋' to 'Nagaas' over there 🐍🐍")
                    return
            else:
                print("Invalid direction! only (left,right or l,w) can be given!")
                return
        except Exception as directionError:
            print(f"Error in handling direction: {directionError}")
        
    def startGame(self):
        try:
            self.printWelcomeMessage()
            self.selectDirection()
        except Exception as startError:
            print(f"Error in starting the game: {startError}")
            
treassureIsland = TreassureIsland()
treassureIsland.startGame()