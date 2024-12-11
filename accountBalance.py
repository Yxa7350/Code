import inputValidator
import math

class Account:
    money = inputValidator.Validator.get_integer("How much money do you have for investment? Between the price range $1250-$20000  - $" ,1250,20000)
    investAmount = math.ceil(money/3)
    print("Amount available for investment - $", investAmount)
    print("Let's begin!")
    