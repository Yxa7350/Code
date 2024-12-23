import main
import days
import yfinance as yf
import graphMaker
import math

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA Corporation"]


class choosing:
    @staticmethod
    def choose(balance):
        while True:
            print(companyList)
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

            choice = input("In which Company would you like to invest?(write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                Ticker = yf.Ticker("NKE")
                graphMaker.fiftyDays(Ticker)
                stockPrice = round(get_stock_price(Ticker, startDate, end), 2)
                print("Current Nike stock price:-   $", stockPrice)
                sure = input("Are you sure you want to buy", Ticker, "Stock? (y/n)    ")
                if sure == "y":
                    maxBuy = math.floor(main.availableInvestment/ stockPrice)
                    print("How much Stock do you want to buy? (max -", maxBuy, ")")
            elif (choice == "Adidas"):
                break
            elif (choice == "Apple"):
                break
            elif (choice == "Tesla"):
                break
            elif (choice == "S&P 500"):
                break
            elif (choice == "NVIDIA Corporation"):
                break
            elif (choice == "DONE"):
                break
            else:
                print("Please enter a valid company name")