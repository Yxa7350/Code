import yfinance as yf
import asciichartpy

# Use a valid historical date range
start = '2022-01-01'  # Start date
end = '2022-12-31'    # End date

# Download stock data for Google
data = yf.download('GOOG', start=start, end=end)

# Check if data is fetched correctly
if not data.empty:
    prices = data['Close'].tolist()
    # Print the chart
    chart = asciichartpy.plot(prices, {'height': 10})
    print(chart)
else:
    print("No data found for the given date range.")