import yfinance as yf
import plotext as plt
from datetime import datetime
import days

@staticmethod
def fiftyDays(ticker):
    # Ensure the ticker is a string
    if isinstance(ticker, yf.Ticker):
        ticker = ticker.ticker

    # Fetch stock data using yfinance
    data = yf.download(ticker, start=days.Days.fiftyStock, end=days.Days.stockTimeEnd, group_by="ticker")

    # Ensure the 'Close' column exists and is accessed correctly
    if (ticker, "Close") in data.columns:
        closing_prices = data[(ticker, "Close")].tolist()

        # Convert dates to plotext-compatible format
        dates = [datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y") for date in data.index.strftime("%Y-%m-%d").tolist()]

        # Plot using plotext
        plt.clear_data()
        plt.title(f"{ticker} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.plot(dates, closing_prices, label=f"{ticker} Close")
        plt.show()  # Legend will display automatically
    else:
        print(f"Error: 'Close' column not found for ticker {ticker} in the retrieved data.")
