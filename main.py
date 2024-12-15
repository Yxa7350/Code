import companies
import graphMaker
import inputValidator
import days
import accountBalance

print("Welcome to Stock Market Simulator!")
availableInvestment = accountBalance.Account.getMoney()
print("Amount available for investment - $", availableInvestment)
print("Let's begin!")
#companies.Company.showCompanies(availableInvestment, 1)
#chosenCompany= input(print("please choose the company you wish to invest in from", companies.companyList))