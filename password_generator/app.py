import random

class PasswordGenerator:
    def __init__(self):
        
        self.alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.symbols = ['!','@','#','$','%','&','(',')','*','+']
        self.__password = []
        self.__finalPassword = ""
        
    def mergePassword(self):
        try:
            random.shuffle(self.__password)
            for char in self.__password:
                self.__finalPassword += char
            return self.__finalPassword
        except Exception as passwordMergeError:
            print(f"Error in merging the password: {passwordMergeError}")
    
    def getPassword(self,alphCnt,numCnt,symbCnt):
        try:
            for num in range(0,alphCnt):
                self.__password.append(random.choice(self.alphabets))
            
            for num in range(0,numCnt):
                self.__password.append(random.choice(self.numbers))
            
            for num in range(0,symbCnt):
                self.__password.append(random.choice(self.symbols))
            
            finalPass = self.mergePassword()
            return finalPass
        
        except Exception as passwordGenError:
            print(f"Error in generating the password:{passwordGenError}")
            
result = PasswordGenerator()
alphCnt = int(input("Enter the number of alphabets you need:"))
numCnt = int(input("Enter the count of numbers you need to include in password:"))
symbCnt = int(input("Enter the count of symbols you need to include:"))
finalPass = result.getPassword(alphCnt=alphCnt,numCnt=numCnt,symbCnt=symbCnt)
print(finalPass)