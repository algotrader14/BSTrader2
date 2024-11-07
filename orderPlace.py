import time
import datetime
from .kiteTrade import *
from zconnect.models import enctoken


#====Parameter Set ===================================
marketstart='09:15:00'
marketend='15:29:59'
#=====================================================



def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def marketHoursStatus():
    dataToken=enctoken.objects.order_by('-id')[:1]
    for item in dataToken:
        token=item.enctoken
    kite = KiteApp(enctoken=token)

    details =kite.quote("NSE:NIFTY 50")
    #print(details)
    if details:
        timevalue=details['NSE:NIFTY 50']['timestamp']
        #actual= timevalue.strftime('%H:%M:%S')
        actual1=datetime.datetime.strptime(timevalue,'%Y-%m-%d %H:%M:%S')
        actual= actual1.strftime('%H:%M:%S')
        actual_in_sec=get_sec(actual)
        starttime_in_sec=get_sec(marketstart)
        endtime_in_sec=get_sec(marketend)
        #print(actual_in_sec)
        #print(starttime_in_sec)
        #print(endtime_in_sec)
    
        if actual_in_sec > starttime_in_sec and actual_in_sec < endtime_in_sec:
            return_value=1
        else:
            return_value=0
        
        return return_value
    else:
        return 0


def marketTime():
    dataToken=enctoken.objects.order_by('-id')[:1]
    for item in dataToken:
        token=item.enctoken
    kite = KiteApp(enctoken=token)

    details =kite.quote("NSE:NIFTY 50")    

    #print(details)
    if details:
        timevalue=details['NSE:NIFTY 50']['timestamp']
        actual= timevalue.strftime('%H:%M:%S')
    
        return actual
    else:
        return '00:00:00'

def buyOrder(tradingSymbol,Qty,Price):
    print("inside buy Order")
    dataToken=enctoken.objects.order_by('-id')[:1]
    for item in dataToken:
        token=item.enctoken
    kite = KiteApp(enctoken=token)
    
    print("buy Order Block:")

    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NFO,
                         tradingsymbol=tradingSymbol,
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=Qty,
                         product=kite.PRODUCT_NRML,
                         order_type=kite.ORDER_TYPE_LIMIT,
                         price=Price,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")
    
    return order

def sellOrder(tradingSymbol,Qty,Price):
    dataToken=enctoken.objects.order_by('-id')[:1]
    for item in dataToken:
        token=item.enctoken
    kite = KiteApp(enctoken=token)
    print("Order Execute: SELL")
    order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NFO,
                         tradingsymbol=tradingSymbol,
                         transaction_type=kite.TRANSACTION_TYPE_SELL,
                         quantity=Qty,
                         product=kite.PRODUCT_NRML,
                         order_type=kite.ORDER_TYPE_LIMIT,
                         price=Price,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")
    
    return order
