import yfinance as yf
import plotext as plt
from datetime import datetime

# Fetch stock data using yfinance
ticker = "AAPL"  # Example: Apple Inc.
data = yf.download(ticker, start="2023-01-01", end="2023-12-31", group_by="ticker")

# Ensure the 'Close' column exists and is accessed correctly
if (ticker, "Close") in data.columns:
    closing_prices = data[(ticker, "Close")].tolist()

    # Convert dates to plotext-compatible format
    dates = [datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y") for date in data.index.strftime("%Y-%m-%d").tolist()]

    # Plot using plotext
    plt.clear_data()
    plt.title(f"{ticker} Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.plot(dates, closing_prices, label=f"{ticker} Close")
    plt.show()  # Legend will display automatically
else:
    print(f"Error: 'Close' column not found for ticker {ticker} in the retrieved data.")
