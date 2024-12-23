import companies
import accountBalance

print("Welcome to Stock Market Simulator!")
accountBalance.Account.addValue()
availableInvestment = accountBalance.Account.money
print("Amount available for investment - $", availableInvestment)
print("Let's begin!")
companies.choosing.choose(availableInvestment)