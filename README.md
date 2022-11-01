# Yahoo-Finance-API-wrapper

Yahoo-Finance-API-wrapper is a wrapper written in Flask to simplify the results from Yahoo finance API

## Configuration

Write your api key from Yahoo finance inside apiKJey.json

## Dependencies
- [Flask](https://pypi.org/project/Flask/)
- [jsonify](https://pypi.org/project/jsonify/)
- [requests](https://pypi.org/project/requests/)

## Use

### Url
```
[GET] http://127.0.0.1:5000/quote/<symbol>
```
### Response Example

```
{
  "currency": "EUR",
  "shortMarket": "PAR",
  "market": "Paris",
  "shortName": "ETF Emergent,
  "name": "ETF EMergent Markets MSCI",
  "price": 4.6,
  "symbol": "AEEM.PA"
}
```
### Error codes
- 429 - not enough resquests avaliable for you API account
- 404 - symbol not found

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

