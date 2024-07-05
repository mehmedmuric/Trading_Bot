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

#orderbook data

ob = onecall.get_orderbook(symbol, True)
print(ob)