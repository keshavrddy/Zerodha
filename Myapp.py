import urlparse
from flask import Flask
from flask import request
import hashlib
import requests
import json


public_token = ""
app = Flask(__name__)


@app.route('/')
def home():
    request_token = str(request.args.get("request_token"))
    api_key = "dn9ld7rvexwulult"
    api_secret = "cedkw4emw3c8ybdqoewturi131rv42ur"

    # Comes from the redirect parameters.

    print request_token
    h = hashlib.sha256(api_key + request_token + api_secret)
    checksum = h.hexdigest()

    params = {'api_key': api_key, 'request_token': request_token, 'checksum': checksum}
    print params
    response = requests.post('https://api.kite.trade/session/token', params=params)
    json_obj = json.loads(str(response.text))
    print (json_obj['data']['public_token'])
    return str(response.text)


if __name__ == '__main__':
    app.run(debug=True)