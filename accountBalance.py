import inputValidator
import math
import companies
import Player

class Account:
    money = None
    @staticmethod
    def addValue():
        Account.money = inputValidator.Validator.get_integer("How much money do you have for investment? Between the price range $1250-$20000  - $", 1250, 20000)
    
    @staticmethod
    def buyStock(amount, price, name):
        buy = amount*price
        print(f"Bought {amount} {name} stock for ${buy}")
        temp= round(Account.money - buy, 2)
        Account.money = temp
        print("Your Current Account Balance:-   $", Account.money)
        companies.choosing.choose(Account.money)

#    def withdraw(amount):
#        print("how much money do you want to invest in", )
 #       if (Account.money.balance >= amount):
  #          print(str.format("Withdrawing ${:.2f}",amount))
   #         Account.money -= amount
    #    else:
     #       print("Insufficient funds")
   #     return
#    def get_balance():
    #    return Account.money