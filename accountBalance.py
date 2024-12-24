import inputValidator
import math
import companies
import Player

class Account:
    money = None
    @staticmethod
    def addValue():
        Account.money = inputValidator.Validator.get_integer("How much money do you have for investment? Between the price range $1250-$20000  - $", 1250, 20000)
        Player.Stats.startingMoney(Account.money)
    
    @staticmethod
    def buyStock(amount, price, name):
        buy = amount*price
        print(f"Bought {amount} {name} stock for ${buy}")
        Player.Stats.addStock(name, amount)
        temp= round(Account.money - buy, 2)
        Account.money = temp
        print("Your Current Account Balance:-   $", Account.money)
        companies.choosing.choose(Account.money)

    def sellStock(amount, price, name):
        sell = amount*price
        print(f"Sold {amount} {name} stock for ${sell}")
        Player.Stats.sellStock(name, amount)
        temp= round(Account.money + sell, 2)
        Account.money = temp
        print("Your Current Account Balance:-   $", Account.money)
        companies.choosing.choose(Account.money)

    def finalSellStock(amount, price, name):
        sell = amount*price
        Player.Stats.sellStock(name, amount)
        temp= round(Account.money + sell, 2)
        Account.money = temp
