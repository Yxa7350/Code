import inputValidator
import math

class Account:
    print("Welcome to Stock Market Simulator")
    money = inputValidator.Validator.get_integer("How much money do you have for investment? Between the price range $1250-$20000  - $" ,1250,20000)
    print("Amount available for investment - $", money)
    print("Let's begin!")
    