import accountBalance
import companies
import graphMaker
import inputValidator
import days

print("Welcome to Stock Market Simulator")
availableInvestment = accountBalance.Account
print("Amount available for investment - $", accountBalance.Account.money)
print("Let's begin!")
companies.Company.showCompanies(availableInvestment, 1)
chosenCompany= input(print("please choose the company you wish to invest in from", companies.companyList))


