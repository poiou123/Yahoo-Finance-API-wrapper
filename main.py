import json
from flask import Flask
from flask import jsonify
import requests
from flask import Response

app = Flask(__name__)


@app.route("/quote/<simbolo>", methods=['GET'])
def quote(simbolo):
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {
        "symbols": simbolo,
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
        r = Response(response='Limite diário de pedidos excedido', status=429, mimetype="application/json")
        print(429, 'Limite diário de pedidos excedido')
        return r
    else:
        quote = data["quoteResponse"]
        resultado = quote["result"]
        if len(resultado) > 0:
            dictionary = {}
            for i in resultado:
                dictionary = {
                    "moeda": i["currency"],
                    "abreviaturaBolsa": i["exchange"],
                    "nomeBolsa": i["fullExchangeName"],
                    "abreviaturaNome": i["shortName"],
                    "nome": i["longName"],
                    "preco": i["regularMarketPrice"],
                    "simbolo": i["symbol"]
                }
            json_object = json.dumps(dictionary, indent=4)
            r = Response(response=json_object, status=200, mimetype="application/json")
            return r
        else:
            print(404, "Simbolo não encontrado")
            r = Response(response="Simbolo não encontrado", status=404, mimetype="application/json")
            return r


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
