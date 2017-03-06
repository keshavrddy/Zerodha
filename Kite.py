from kiteconnect import KiteConnect
import webbrowser
from flask import Flask, render_template, request
import requests
import hashlib
kite = KiteConnect(api_key="dn9ld7rvexwulult")
webbrowser.open(kite.login_url())
# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

app = Flask(__name__)
req = ""
@app.route('/')

def home():
    req = request.args.get("request_token")
    api_key = "dn9ld7rvexwulult"
    api_secret = "cedkw4emw3c8ybdqoewturi131rv42ur"

    # Comes from the redirect parameters.
    request_token = req

    h = hashlib.sha256(api_key + request_token + api_secret)
    checksum = h.hexdigest()
    print req
    params = {'api_key':'dn9ld7rvexwulult', 'request_token':req, 'checksum': checksum}
    response = requests.post('https://api.kite.trade/session/token', params=params)
    return str(response.status_code)

print req
if __name__ == '__main__':

    app.run(debug=True)
# data = kite.request_access_token("request_token_here", secret="your_secret")
# kite.set_access_token(data["access_token"])
