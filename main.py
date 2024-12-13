import accountBalance
import companies
import graphMaker
import inputValidator
import days

availableInvestment = accountBalance.Account
companies.Company(availableInvestment, 1)
print("Welcome to Stock Market Simulator")
print("Amount available for investment - $", accountBalance.Account.money)
print("Let's begin!")
chosenCompany= input(print("please choose the company you wish to invest in from", companies.companyList))


