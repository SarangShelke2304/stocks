import requests

# url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=SBIN&apikey='
# r = requests.get(url)
# data = r.json()

# print(data)

def search_listing(stock_name :str, api_key :str) -> str:
    """
    Search for a stock listing by name.
    
    Args:
        stock_name (str): The name of the stock to search for.
        api_key (str): Your Alpha Vantage API key.
        
    Returns:
        str: The stock symbol if found, otherwise an empty string.
    """
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock_name}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    
    if 'bestMatches' in data and len(data['bestMatches']) > 0:
        return data['bestMatches'][0]['1. symbol']
    
    return ''