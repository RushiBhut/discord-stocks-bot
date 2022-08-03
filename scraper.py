from bs4 import BeautifulSoup
import requests

# Finds the price of a stock by using the stock's ticker symbol
def find_price(arg):
    symbol = arg.upper()

    # Uses the stock's ticker symbol to create a URL and sends a request to that URL to parse it
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
    result = requests.get(url).text
    page = BeautifulSoup(result, "html.parser")

    # Locates the price of the stock by finding this HTML class which contains the price
    price_class = page.find(class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
    price = price_class["value"]
    
    return price

# Finds the top 10 gaining stocks of the day
def find_gainers():
    url = "https://finance.yahoo.com/gainers"
    result = requests.get(url).text
    page = BeautifulSoup(result, "html.parser")

    # Finds the contents of the table that contains the list of gaining stocks
    tbody = page.tbody
    trs = tbody.contents
    gainers = []
    
    # Loops through the first 10 rows in the table and finds the name, ticker symbol, and percent change for each stock
    for tr in trs[:10]:
        name = tr.contents[1].contents[0]
        symbol = tr.contents[0].find("a").contents[0]
        percent_change = tr.contents[4].find("span").contents[0]
        data = [name, symbol, percent_change]
        gainers.append(data)
    
    return gainers

# Finds the top 10 losing stocks of the day
def find_losers():
    url = "https://finance.yahoo.com/losers"
    result = requests.get(url).text
    page = BeautifulSoup(result, "html.parser")

    # Finds the contents of the table that contains the list of losing stocks
    tbody = page.tbody
    trs = tbody.contents
    losers = []

    # Loops through the first 10 rows in the table and finds the name, ticker symbol, and percent change for each stock
    for tr in trs[:10]:
        name = tr.contents[1].contents[0]
        symbol = tr.contents[0].find("a").contents[0]
        percent_change = tr.contents[4].find("span").contents[0]
        data = [name, symbol, percent_change]
        losers.append(data)

    return losers
