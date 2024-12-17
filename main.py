import companies
import inputValidator
import days
import accountBalance

print("Welcome to Stock Market Simulator!")
availableInvestment = accountBalance.Account.getMoney()
print("Amount available for investment - $", availableInvestment)
print("Let's begin!")
companies.choosing.choose(availableInvestment, 1)