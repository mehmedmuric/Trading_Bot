import pandas as pd #excel for python
import onecall #handling data
import time #time
import schedule

# import file api

size = 1   
symbol = 'USDCAD'

onecall = onecall.phemex(
    key = 'adadada',
    secret = 'sadadsads',
)

def ask_bid(symbol=symbol):
#orderbook data
    ob = onecall.get_orderbook(symbol, True)
    ask = ob['result']['book']['asks'][0][0]
    bid = ob['result']['book']['bids'][0][0]
    print(f'this bid {bid} ask {ask}')

    return ask, bid, ob


# make the buy and sell order function
def bot():

    askbid = ask_bid(symbol)
    ask = askbid[0]
    bid = askbid[1]
    #making a buy order
    onecall.limit_order(symbol, onecall.BUY_SIDE, size, bid)

    #making a sell order
    onecall.limit_order(symbol, onecall.SELL_SIDE, size, ask)


bot()
#identify the biggest movers % up and down


# 1. find the biggest movers and lowest movers
    # % gain and % lost - the biggest ones




# 2. check the SMAs to see if we should be longing/shorting    
    # long if over 1hr sma, and short if under the 1hr sma



# 3. when to enter? if long on a pull back and short, rip