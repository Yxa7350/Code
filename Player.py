import companies
import days
import accountBalance
import yfinance as yf
import datetime

class Stats:
    Nike = 0
    Adidas = 0
    Apple = 0
    Tesla = 0
    SP500 = 0
    Nvidia = 0
    startingBalance = 0
    finalBalance = 0
    @staticmethod
    def startingMoney(amount):
        Stats.startingBalance = amount
    startDate = datetime.date.today() + datetime.timedelta(1)
    endDate = datetime.date.today()
    @staticmethod
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
    @staticmethod
    def addStock(name, amount):
            if (name == "Nike"):
                Stats.Nike += amount
            elif (name == "Adidas"):
                Stats.Adidas += amount
            elif (name == "Apple"):
                Stats.Apple += amount
            elif (name == "Tesla"):
                Stats.Tesla += amount
            elif (name == "S&P 500"):
                Stats.SP500 += amount
            elif (name == "NVIDIA"):
                Stats.Nvidia += amount
    @staticmethod
    def sellStock(name, amount):
            if (name == "Nike"):
                Stats.Nike -= amount
            elif (name == "Adidas"):
                Stats.Adidas -= amount
            elif (name == "Apple"):
                Stats.Apple -= amount
            elif (name == "Tesla"):
                Stats.Tesla -= amount
            elif (name == "S&P 500"):
                Stats.SP500 -= amount
            elif (name == "NVIDIA"):
                Stats.Nvidia -= amount
    @staticmethod
    def end():
        Ticker = yf.Ticker("NKE")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.Nike
        accountBalance.Account.sellStock(maxSell, stockPrice, "Nike")
        Ticker = yf.Ticker("ADDYY")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.Adidas
        accountBalance.Account.sellStock(maxSell, stockPrice, "Adidas")
        Ticker = yf.Ticker("AAPL")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.Apple
        accountBalance.Account.sellStock(maxSell, stockPrice, "Apple")
        Ticker = yf.Ticker("TSLA")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.Tesla
        accountBalance.Account.sellStock(maxSell, stockPrice, "Tesla")
        Ticker = yf.Ticker("^GSPC")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.SP500
        accountBalance.Account.sellStock(maxSell, stockPrice, "S&P 500")
        Ticker = yf.Ticker("NVDA")
        stockPrice = round(Stats.get_stock_price(Ticker, Stats.startDate, Stats.endDate), 2)
        maxSell = Stats.Nvidia
        accountBalance.Account.sellStock(maxSell, stockPrice, "NVIDIA")
    

    @staticmethod
    def show(balance):
        print(f"End of Day {days.Days.gameDay} Stats")
        print("Your Account balance :-  $", balance)
        print(f"You own {Stats.Nike} Nike Stocks")
        print(f"You own {Stats.Adidas} Adidas Stocks")
        print(f"You own {Stats.Apple} Apple Stocks")
        print(f"You own {Stats.Tesla} Tesla Stocks")
        print(f"You own {Stats.SP500} S&P 500 Stocks")
        print(f"You own {Stats.Nvidia} NVIDIA Stocks")
        print("10 Days Later...")
        companies.choosing.choose(balance)