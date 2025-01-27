from cipherAlpha import alphabets
from art import logo

class Security:
    def __init__(self):
        print("Welcome to Caesar Cipher 🙏")
        print(logo)
        self.__alphabets = alphabets
        self.__shouldContinue = True
        
    def caesar_cipher(self,original_text,shift_number,direction):
        try:
            __output_text = ""
            if direction == "decode":
                shift_number *= -1
            for letter in original_text:
                if letter not in self.__alphabets:
                    __output_text += letter
                else:
                    shift_position = self.__alphabets.index(letter) + shift_number
                    shift_position %= len(self.__alphabets)
                    __output_text += self.__alphabets[shift_position]
            print(f"Here is the {direction}d text: {__output_text}")
        except Exception as encodeDecodeError:
            print(f"Error in performing caesarCipher: {encodeDecodeError}")
            
    def start(self):
        while self.__shouldContinue:
            direction = input("Type 'Encode' to encrypt or type 'Decode' to decrypt:")
            text = input(f"Enter the text you want to {direction}:")
            shiftNum = int(input("Enter the shift amount:"))
            self.caesar_cipher(text,shiftNum,direction.lower())
            continueOrNot = input("Type 'Yes' if you would like to continue or type 'No':")
            if continueOrNot.lower() == 'no':
                print("Bye👋 see you again soon!")
                self.__shouldContinue = False

obj = Security()
obj.start()
    