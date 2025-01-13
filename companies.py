import days
import yfinance as yf
import graphMaker
import math
import inputValidator
import accountBalance
import Player
import datetime
import warnings

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA"]


class choosing:
    @staticmethod
    def choose(balance):
        while True:
            print("Your Options :-", companyList[0],",", companyList[1],",", companyList[2],",", companyList[3],",", companyList[4],",", companyList[5])
            startDate = days.Days.stockTimeStart
            end = days.Days.stockTimeEnd
            def get_stock_price(ticker, start_date, end_date):
                # Ensure the provided object is a valid yfinance Ticker
                if not isinstance(ticker, yf.Ticker):
                    raise ValueError("ticker must be an instance of yfinance.Ticker")

                # Suppress yfinance warnings
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=UserWarning, module="yfinance")

                    # Get historical market data for the specific date range
                    historical_data = ticker.history(start=start_date, end=end_date)

                # Check if data is available for the given date range
                if not historical_data.empty:
                    # Retrieve the closing price for the last available day in the range
                    closing_price = historical_data['Close'].iloc[-1]
                    return closing_price
                else:
                    # Fetch data for the nearest previous trading day
                    with warnings.catch_warnings():
                        warnings.filterwarnings("ignore", category=UserWarning, module="yfinance")
                        historical_data = ticker.history(period='5d')  # Fetch last 5 days of data

                    if not historical_data.empty:
                        closing_price = historical_data['Close'].iloc[-1]  # Most recent closing price
                        return closing_price
                    else:
                        return None  # No data available at all
            def interaction(name, Ticker):
                graphMaker.fiftyDays(Ticker)
                stockPrice = round(get_stock_price(Ticker, startDate, end), 2)
                print(f"Current {name} stock price:-   $", stockPrice)
                sure = input(f"Are you sure you want to buy {name} Stock? (y/n)    ")
                if sure == "y":
                    maxBuy = math.floor(balance/ stockPrice)
                    amountBuy = inputValidator.Validator.get_integer(f"How much Stock do you want to buy? (max - {maxBuy})    ", 0, maxBuy)
                    accountBalance.Account.buyStock(amountBuy, stockPrice, name)
                print("Proceeding to sell page")
                if name == "S&P 500":
                        maxSell = getattr(Player.Stats, "SP500") #Exceptions
                elif name == "NVIDIA":
                        maxSell = getattr(Player.Stats, "Nvidia")  #Exceptions
                else:
                        maxSell = getattr(Player.Stats, name)
                amountSell = inputValidator.Validator.get_integer(f"How much Stock do you want to sell? (max - {maxSell})    ", 0, maxSell)
                accountBalance.Account.sellStock(amountSell, stockPrice, name)

            choice = input("In which Company would you like to invest?  (write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                name = "Nike"
                Ticker = yf.Ticker("NKE")
                interaction(name, Ticker)
                break
            elif (choice == "Adidas"):
                name = "Adidas"
                Ticker = yf.Ticker("ADDYY")
                interaction(name, Ticker)
                break
            elif (choice == "Apple"):
                name = "Apple"
                Ticker = yf.Ticker("AAPL")
                interaction(name, Ticker)
                break
            elif (choice == "Tesla"):
                name = "Tesla"
                Ticker = yf.Ticker("TSLA")
                interaction(name, Ticker)
                break
            elif (choice == "S&P 500"):
                name = "S&P 500"
                Ticker = yf.Ticker("^GSPC")
                interaction(name, Ticker)
                break
            elif (choice == "NVIDIA"):
                name = "NVIDIA"
                Ticker = yf.Ticker("NVDA")
                interaction(name, Ticker)
                break
            elif (choice == "DONE"):
                if days.Days.today == (days.Days.stockTimeEnd):
                    Player.Stats.end()
                    break
                else:
                    days.Days.add_days()
                    Player.Stats.show(balance)
                    break
            else:
                print("Please enter a valid company name")