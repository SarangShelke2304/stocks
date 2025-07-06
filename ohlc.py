import requests
from datetime import datetime, timedelta


def get_ohlc_data(symbol: str, api_key: str) -> str:
    """
    Fetch OHLC data for a given stock symbol from Alpha Vantage.
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('Time Series (Daily)', {})
        if not data:
            return "No data found for the given symbol."
        # Get the most recent trading day
        today = datetime.now()
        last_trading_day = today - timedelta(days=(today.weekday() + 1) % 5)    
        last_trading_date = last_trading_day.strftime('%Y-%m-%d')
        last_candle = data.get(last_trading_date)
        if last_candle:
            o = last_candle["1. open"]
            h = last_candle["2. high"]
            l = last_candle["3. low"]
            c = last_candle["4. close"]
            return f"Last trading day ({last_trading_date}) – O/H/L/C: {o}, {h}, {l}, {c}"
        else:
            return "No data for last trading day"
    else:
        return f"Error fetching data: {response.status_code}"
        


# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SBIN.BSE&apikey=QFYT9BLL9AJZA5VN'
# r = requests.get(url)
# data = r.json().get('Time Series (Daily)', {})

# # get today's date
# from datetime import datetime, timedelta
# today = datetime.now()
# # get the last trading day (assuming it's a weekday)
# last_trading_day = today - timedelta(days=(today.weekday() + 1) % 5)    
# # get the date in YYYY-MM-DD format
# last_trading_date = last_trading_day.strftime('%Y-%m-%d')
# # print the last trading date
# print("Last trading date:", last_trading_date)
# # get the OHLC data for the last trading day
# last_candle = data.get(last_trading_date)
# if last_candle:
#     o = last_candle["1. open"]
#     h = last_candle["2. high"]
#     l = last_candle["3. low"]
#     c = last_candle["4. close"]
#     print(f"Last trading day ({last_trading_date}) – O/H/L/C:", o, h, l, c)
# else:
#     print("No data for last trading day")
# monday_candle = data.get("2025-06-06")
# if monday_candle:
#     o = monday_candle["1. open"]
#     h = monday_candle["2. high"]
#     l = monday_candle["3. low"]
#     c = monday_candle["4. close"]
#     print("2025-06-06 – O/H/L/C:", o, h, l, c)
# else:
#     print("No data for Monday 16:30")   