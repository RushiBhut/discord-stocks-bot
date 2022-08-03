from bs4 import BeautifulSoup
import requests

# Finds the price of a stock by using the stock's ticker symbol
def find_price(arg):
    symbol = arg.upper()

    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
    result = requests.get(url).text
    page = BeautifulSoup(result, "html.parser")

    price_class = page.find(class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
    price = price_class["value"]
    
    return price

# Finds the top 10 gaining stocks of the day
def find_gainers():
    url = "https://finance.yahoo.com/gainers"
    result = requests.get(url).text
    page = BeautifulSoup(result, "html.parser")

    tbody = page.tbody
    trs = tbody.contents
    gainers = []
    
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

    tbody = page.tbody
    trs = tbody.contents
    losers = []

    for tr in trs[:10]:
        name = tr.contents[1].contents[0]
        symbol = tr.contents[0].find("a").contents[0]
        percent_change = tr.contents[4].find("span").contents[0]
        data = [name, symbol, percent_change]
        losers.append(data)

    return losers
