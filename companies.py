import random
import math
import days
import yfinance as yf

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA Corporation"]


class choosing:
    @staticmethod
    def choose(balance):
        while True:
            print(companyList)
            startDate = "2024-11-14"
            end = "2024-11-15"
            def get_stock_price(ticker_symbol, date):
                # Create a Ticker object
                ticker = yf.Ticker(ticker_symbol)

                # Get historical market data for the specific date
                historical_data = ticker.history(start=date, end=date)

                # Check if data is available for the given date
                if not historical_data.empty:
                    # Retrieve the closing price using iloc
                    closing_price = historical_data['Close'].iloc[0]
                    return closing_price
                else:
                    return None  # No data for the given date

            def get_stock_volume(ticker_symbol, date):
                # Create a Ticker object
                ticker = yf.Ticker(ticker_symbol)

                # Get historical market data for the specific date
                historical_data = ticker.history(start=date, end=date)

                # Check if data is available for the given date
                if not historical_data.empty:
                    # Retrieve the volume using iloc
                    volume = historical_data['Volume'].iloc[0]
                    return volume
                else:
                    return None  # No data for the given date

            choice = input("In which Company would you like to invest?(write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                Nike = yf.Ticker("nke")
                print("Current Nike stock price:-", get_stock_price(Nike, startDate, end))
                print("Current Nike stock volume:-", get_stock_volume(Nike, startDate, end))
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