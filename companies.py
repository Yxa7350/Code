import random
import math

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA Corporation"]

class Company:
    type = None
    type1 = random.randrange(1,4) # Types include Small, Medium, and Large volume of shares
    type2 = random.randrange(1,4) # Types include Common, Value, and Growth for each share
    def __init__(self):
        if (self.type1 == 1) and (self.type2 == 1):
            self.type = 1
        elif (self.type1 == 1) and (self.type2 == 2):
            self.type = 2
        elif (self.type1 == 1) and (self.type2 == 3):
            self.type = 3
        elif (self.type1 == 2) and (self.type2 == 1):
            self.type = 4
        elif (self.type1 == 2) and (self.type2 == 2):
            self.type = 5
        elif (self.type1 == 2) and (self.type2 == 3):
            self.type = 6
        elif (self.type1 == 3) and (self.type2 == 1):
            self.type = 7
        elif (self.type1 == 3) and (self.type2 == 2):
            self.type = 8
        elif (self.type1 == 3) and (self.type2 == 3):
            self.type = 9


Nike = Company()
Adidas = Company()
Apple = Company()
Tesla = Company()
Sp500 = Company()
Nvidia = Company()

class choosing:
    @staticmethod
    def choose(balance, day):
        while True:
            print(companyList)
            choice = input("In which Company would you like to invest?(write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                stockType = Nike.type
                if stockType == 1:
                    stockVolume = random.randrange(50,201)
                    stockPrice = random.randrange(1, )
                print("Current Nike stock price:-", )
                print("Current Nike stock volume:-", )
            elif (choice == "Adidas"):
                break
            elif (choice == "Apple"):
                break
            elif (choice == "Tesla"):
                break
            elif (choice == "S&P 500"):
                break
            elif (choice == "NVIDIA Corporation"):
                break
            elif (choice == "DONE"):
                break
            else:
                print("Please enter a valid company name")