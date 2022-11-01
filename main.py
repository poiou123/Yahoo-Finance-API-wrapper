import json
from flask import Flask
from flask import jsonify
import requests
from flask import Response

app = Flask(__name__)


@app.route("/quote/<symbol>", methods=['GET'])
def quote(symbol):
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {
        "symbols": symbol,
        "region": "PT",
        "lang": "en"
    }
    keyFile = open("apiKey.json")
    apiKeyJson=json.load(keyFile)
    apiKey=apiKeyJson["apiKey"]
    headers = {
        'X-API-KEY': apiKey,
        'accept': "application/json",
        'User-Agent': '',
        'Accept-Encoding': '',
        'Connection': ''
    }
    keyFile.close()
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonSTR = response.content
    data = json.loads(jsonSTR)
    if data["message"] == "Limit Exceeded":
        r = Response(response='Daily request limit reached', status=429, mimetype="application/json")
        print(429, 'Daily request limit reached')
        return r
    else:
        quote = data["quoteResponse"]
        result = quote["result"]
        if len(result) > 0:
            dictionary = {}
            for i in result:
                dictionary = {
                    "currency": i["currency"],
                    "shortMarket": i["exchange"],
                    "market": i["fullExchangeName"],
                    "shortName": i["shortName"],
                    "name": i["longName"],
                    "price": i["regularMarketPrice"],
                    "symbol": i["symbol"]
                }
            json_object = json.dumps(dictionary, indent=4)
            r = Response(response=json_object, status=200, mimetype="application/json")
            return r
        else:
            print(404, "Symbol not found")
            r = Response(response="Symbol not found", status=404, mimetype="application/json")
            return r


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
