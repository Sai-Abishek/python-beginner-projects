import os
from art import logo

class SecretAuction:
    def __init__(self):
        print("🙏 Welcome to Auction Process 🙏")
        print(logo)
        self.__should_run = True
        
    def getTheWinner(self,bid_dictionary):
        __winner = ""
        __highest_bid = 0
        try:
            for key,value in bid_dictionary.items():
                if value > __highest_bid:
                    __highest_bid = value
                    __winner = key
            print(f"🏆🏆 The winner is {__winner} with the bid of ${__highest_bid} 🏆🏆")
        except Exception as analysisError:
            print(f"Error in getting the winner: {analysisError}")
    
    def clearScreen(self):
        try:
            os.system('cls')
        except Exception as clearScreenError:
            print(f"Error in clearing the screen: {clearScreenError}")
                
    def start(self):
        __bid_list = {}
        while self.__should_run:
            name = input("Enter your name:")
            bid_amount = int(input("Enter the bid amount: $"))
            __bid_list[name] = bid_amount
            shouldRun = input("Is there any other person in bid? ('yes' or 'no'):").lower()
            if shouldRun == 'no':
                self.__should_run = False
                self.getTheWinner(__bid_list)
            else:
                self.clearScreen()
                
obj = SecretAuction()
obj.start()