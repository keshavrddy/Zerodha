#!/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7
from kiteconnect import WebSocket


# Initialise.
kws = WebSocket("dn9ld7rvexwulult", "ged1jukz0odgwt6mcqmsxyy5tvomxh4khujkhd", "RK0562")

# Callback for tick reception.
def on_tick(tick, ws):
    print tick

# Callback for successful connection.
def on_connect(ws):
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    # ws.subscribe([53406215])
    # ws.subscribe([53395463])
    ws.subscribe([53382407])
    # ws.set_mode((ws.MODE_QUOTE,[53427463]))
    # Set RELIANCE to tick in `full` mode.
    # ws.set_mode(ws.MODE_QUOTE, [738561])
    # ws.set_mode(ws.MODE_QUOTE, [5633])

# Assign the callbacks.
kws.on_tick = on_tick
kws.on_connect = on_connect

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()