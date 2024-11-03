from constants import coaster_const

class CheckEligibility:
    def __init__(self):
        self.category = None
        
    def verifyHeight(self,height):
        return True if height >= coaster_const['minHeight'] else False

    def verifyAge(self,age):
        try:
            if age < 12:
                self.category = "children"
            elif age >=12 and age <=18:
                self.category = "youths"
            else:
                self.category = "adults"
            return self.category
        except Exception as ageError:
            print(f'Error in age verification: {ageError}')

class RollerCoster(CheckEligibility):
    def __init__(self,height,age):
        self.height = self.verifyHeight(height)
        self.cat = self.verifyAge(age)
        self.price = 0

    def getTicketPrice(self):
        try:
            if self.height:
                self.price += coaster_const['price'][self.cat]
                print(f"Total fare: ${self.price}")
                photo = input("Do you want to take a photo? (Y or N):")
                if photo.lower().startswith('y'):
                    proceed = input("Photo adds +$3 to your total fare, Do you wish to continue? (Y or N):")
                    if proceed.lower().startswith('y'):
                        self.price += 3
                return self.price
            else:
                return f"Sorry! you can't ride the coaster, your height should be {coaster_const['minHeight']}cm+"
        except Exception as ticketPriceError:
            print(f"Error in getting ticket fare:{ticketPriceError}")
            
print("Welcome to roller coster ride 🎉🛤️\n")
height = float(input("Enter your height in (cm):"))
age = float(input("Enter your age:"))
rider = RollerCoster(round(height),round(age))
ticketPrice = rider.getTicketPrice()
print(f"Final ticket fare: ${ticketPrice}") if type(ticketPrice) == int else print(f"OOPS! {ticketPrice}")