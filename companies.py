import random
import math
import days
import yfinance as yf

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA Corporation"]

class choosing:
    @staticmethod
    def choose(balance, day):
        while True:
            print(companyList)
            choice = input("In which Company would you like to invest?(write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                Nike = yf.Ticker("nke")
                print("Current Nike stock price:-", )
                print("Current Nike stock volume:-", Nike.info["volume"])
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