import random
import days
import yfinance as yf

companyList = ["Nike", "Adidas", "Apple", "Tesla", "S&P 500", "NVIDIA Corporation"]


class choosing:
    @staticmethod
    def choose(balance):
        while True:
            print(companyList)
            startDate = "2024-11-15"
            end = "2024-11-16"
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

            def get_stock_volume(ticker, start_date, end_date):
                # Get historical market data for the specific date range
                historical_data = ticker.history(start=start_date, end=end_date)

                # Check if data is available for the given date range
                if not historical_data.empty:
                    # Retrieve the volume for the last day in the range
                    volume = historical_data['Volume'].iloc[-1]  # Get the last day's volume
                    return volume
                else:
                    return None  # No data for the given date range

            choice = input("In which Company would you like to invest?(write \"DONE\" if you are done)  ")
            if (choice == "Nike"):
                Nike = yf.Ticker("nke")
                print("Current Nike stock price:-   $", round(get_stock_price(Nike, startDate, end), 2))
                print("Current Nike stock volume:-  ", get_stock_volume(Nike, startDate, end))
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