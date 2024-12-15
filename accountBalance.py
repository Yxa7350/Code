import inputValidator
import math
import companies
class Account:
    money = inputValidator.Validator.get_integer("How much money do you have for investment? Between the price range $1250-$20000  - $" ,1250,20000)
    
    def deposit(amount):
        print(str.format("Depositing ${:.2f}",amount))
        Account.money += amount
        return
    
    def withdraw(amount):
        print("how much money do you want to invest in", )
        if (Account.money.balance >= amount):
            print(str.format("Withdrawing ${:.2f}",amount))
            Account.money -= amount
        else:
            print("Insufficient funds")
        return
    def get_balance():
        return Account.money