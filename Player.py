import companies
import days

class Stats:
    Nike = 0
    Adidas = 0
    Apple = 0
    Tesla = 0
    SP500 = 0
    Nvidia = 0
    startingBalance = 0
    finalBalance = 0
    @staticmethod
    def startingMoney(amount):
        Stats.startingBalance = amount
    @staticmethod
    def addStock(name, amount):
            if (name == "Nike"):
                Stats.Nike += amount
            elif (name == "Adidas"):
                Stats.Adidas += amount
            elif (name == "Apple"):
                Stats.Apple += amount
            elif (name == "Tesla"):
                Stats.Tesla += amount
            elif (name == "S&P 500"):
                Stats.SP500 += amount
            elif (name == "NVIDIA"):
                Stats.Nvidia += amount
    @staticmethod
    def sellStock(name, amount):
            if (name == "Nike"):
                Stats.Nike -= amount
            elif (name == "Adidas"):
                Stats.Adidas -= amount
            elif (name == "Apple"):
                Stats.Apple -= amount
            elif (name == "Tesla"):
                Stats.Tesla -= amount
            elif (name == "S&P 500"):
                Stats.SP500 -= amount
            elif (name == "NVIDIA"):
                Stats.Nvidia -= amount
    @staticmethod
    def end():
        pass
    @staticmethod
    def show(balance):
        print(f"End of Day {days.Days.gameDay} Stats")
        print("Your Account balance :-  $", balance)
        print(f"You own {Stats.Nike} Nike Stocks")
        print(f"You own {Stats.Adidas} Adidas Stocks")
        print(f"You own {Stats.Apple} Apple Stocks")
        print(f"You own {Stats.Tesla} Tesla Stocks")
        print(f"You own {Stats.SP500} S&P 500 Stocks")
        print(f"You own {Stats.Nvidia} NVIDIA Stocks")
        print("10 Days Later...")
        companies.choosing.choose(balance)