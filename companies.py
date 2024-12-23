import days
import yfinance as yf
import graphMaker
import math
import inputValidator
import accountBalance

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA"]


class choosing:
    @staticmethod
    def choose(balance):
        while True:
            print("Your Options :-", companyList[0],",", companyList[1],",", companyList[2],",", companyList[3],",", companyList[4],",", companyList[5])
            startDate = days.Days.stockTimeStart
            end = days.Days.stockTimeEnd
            def get_stock_price(ticker, start_date, end_date):
                # Get historical market data for the specific date range
                historical_data = ticker.history(start=start_date, end=end_date)

                # Check if data is available for the given date range
                if not historical_data.empty:
                    # Retrieve the closing price for the last day in the range
                    closing_price = historical_data['Close'].iloc[-1]  # Get the last day's price
                    return closing_price
                else:
                    return None  # No data for the given date range

            choice = input("In which Company would you like to invest?  (write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                Ticker = yf.Ticker("NKE")
                graphMaker.fiftyDays(Ticker)
                stockPrice = round(get_stock_price(Ticker, startDate, end), 2)
                print("Current Nike stock price:-   $", stockPrice)
                sure = input(f"Are you sure you want to buy {"Nike"} Stock? (y/n)    ")
                if sure == "y":
                    maxBuy = math.floor(balance/ stockPrice)
                    amountBuy = inputValidator.Validator.get_integer(f"How much Stock do you want to buy? (max - {maxBuy})    ", 1, maxBuy)
                    accountBalance.Account.buyStock(amountBuy, stockPrice, "Nike")
                    break
            elif (choice == "Adidas"):
                break
            elif (choice == "Apple"):
                break
            elif (choice == "Tesla"):
                break
            elif (choice == "S&P 500"):
                break
            elif (choice == "NVIDIA"):
                break
            elif (choice == "DONE"):
                break
            else:
                print("Please enter a valid company name")