import companies
import accountBalance

print("Welcome to Stock Market Simulator!")
availableInvestment = accountBalance.Account.getMoney()
print("Amount available for investment - $", availableInvestment)
print("Let's begin!")
companies.choosing.choose(availableInvestment)