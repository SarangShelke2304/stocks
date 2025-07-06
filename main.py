from dotenv import load_dotenv
import os

load_dotenv()
from search import search_listing
from ohlc import get_ohlc_data

def main():
    api_key = os.getenv('APIKEY')
    if not api_key:
        print("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")
        return
    stock_name = input("Enter the stock name to search: ")
    symbol = search_listing(stock_name, api_key)
    if not symbol:
        print(f"No stock found for '{stock_name}'.")
        return
    print(f"Found stock symbol: {symbol}")
    ohlc_data = get_ohlc_data(symbol, api_key)
    print(ohlc_data)

if __name__ == "__main__":
    main()