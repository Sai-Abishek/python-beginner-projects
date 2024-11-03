from prettytable import PrettyTable

class ToppingsGuide:
    def toppingsMap(self):
        return {1: 'pepperoni',2: 'olives',3: 'mushrooms',4: 'veggies'}

class Charts:
    def priceChart(self):
        return {
            'size': {'s':10,'m':20,'l':30},
            'toppings':{'pepperoni':10,'olives':30,'mushroom':15,'veggies':20},
            'extra_cheese':10
        }

class pizzaDelivery(ToppingsGuide,Charts):
    def __init__(self,size:str='M',toppings:str='4',extra_cheese:str='N'):
        self.size = size.lower()
        self.toppings = self.toppingsMap().get(int(toppings),None)
        self.extraCheese = extra_cheese.lower()
        self.price = 0

    def getFinalBill(self,pizzaSize,toppingsAdded,extraCheese,finalPrice):
        print("........ Please Collect your bill ........\n")
        billTable = PrettyTable(["Pizza Size", "Toppings", "Extra Cheese", "Amount"])
        billTable.add_row([pizzaSize,toppingsAdded, extraCheese, f"${finalPrice}"])
        return billTable
        
    def calculate_price(self):
        priceChart = self.priceChart()
        try:
            if self.size in priceChart['size']:
                self.price = priceChart['size'][self.size]
                if self.toppings:
                    price = priceChart['toppings'][self.toppings]
                    self.price += price
                else:
                    return "Invalid topping selected: please select any option btwn 1 and 4"
                    self.price = 0
                    return self.price
                if self.extraCheese == 'y':
                    self.price += priceChart['extra_cheese']
                finalbill = self.getFinalBill(self.size.upper(),self.toppings.capitalize(),self.extraCheese.upper(),self.price)
                return finalbill
            else: 
                return "Please enter the valid option (S,M or L)!"
        except Exception as calculationError:
            print(calculationError)
            

print("Welcome to pizza delivery 🍕\n")
size = input("What size of pizza do you want? (S,M or L):")
pepperoni = input("What topping do you want?\n1:Pepperoni\n2:Olives\n3:Mushroom\n4:Veggies\nEnter the option (1,2,3 or 4):")
extraCheese = input("Do you want to add extra cheese? (Y or N):")

pizzaProject = pizzaDelivery(size,pepperoni,extraCheese)
price = pizzaProject.calculate_price()
print(price)
