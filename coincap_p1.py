import os
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tkinter import *

pycrypto =  Tk()
pycrypto.resizable(False, False)
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('logo.ico')

def font_color(amount):
    if amount >=0:
        return "green"
    else:
        return "red"

def my_portfolio():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '',
    }

    parameters = {

    'start': '1',
    'limit': '100',

    }

    coins = [
        {
        "symbol": "BTC",
        "amount_owned": 0.4,
        "price_per_coin": 9000
        },
        {
        "symbol": "ETH",
        "amount_owned": 10,
        "price_per_coin": 170
        },
        {
            "symbol": "XRP",
            "amount_owned": 100,
            "price_per_coin": 0.61
        },
        {
            "symbol": "ADA",
            "amount_owned": 1000,
            "price_per_coin": 0.04
        }
    ]

    session = Session()
    session.headers.update(headers)

    response = session.get(url)
    results = json.loads(response.content)

    total_pl = 0
    coin_row = 1
    total_portfolio_value=0


    for i in range(0, 100):
        for coin in coins:
            if results["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * results["data"][i]["quote"]["USD"]["price"]
                pl_percoin = results["data"][i]["quote"]["USD"]["price"] - coin['price_per_coin']
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl = total_pl + total_pl_coin
                total_portfolio_value = total_portfolio_value + current_value

                name = Label(pycrypto, text=results["data"][i]["name"], bg="#F3F4F6", fg="black", font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="Price - ${0:.2f}".format(results["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black", font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text=total_paid, bg="#F3F4F6", fg="black", font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text= "${0:.2f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
                totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1
#print(json.dumps(results, indent=4))
    totalpv = Label(pycrypto, text="${0:.2f}".format(total_portfolio_value), bg="#F3F4F6", fg="black", font="Lato 9",borderwidth=2, relief="groove", padx="2", pady="2")
    totalpv.grid(row=coin_row, column=4, sticky=N + S + E + W)

    totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 9", borderwidth=2, relief="groove", padx="2", pady="2")
    totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

    results = ""

    update = Button(pycrypto, text="Update", bg="#FFA500", fg="black", command=my_portfolio, font="Lato 12", borderwidth=2, relief="groove", padx="5", pady="5")
    update.grid(row=coin_row + 1, column=6, sticky=N + S + E + W)



name = Label(pycrypto, text="Coin Name", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(pycrypto, text="Coin Owned", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
no_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text="Total Amount Paid", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text="Current Value", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text="P/L Per Coin", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text="Total P/L With Coin", bg = "#FFA500", fg = "white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="raised")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()
print("Program Completed")
