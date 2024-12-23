class Stats:
    Nike = 0
    Adidas = 0
    Apple = 0
    Tesla = 0
    SP500 = 0
    NVIDIA = 0
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
                Stats.NVIDIA += amount
    @staticmethod
    def sellStock(name, amount):
        pass