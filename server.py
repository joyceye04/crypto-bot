from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ["PORT"])
print(port)

@app.route('/', methods=['POST'])
def index():
  print(port)
  data = json.loads(request.get_data())

  # FETCH THE CRYPTO NAME
  crypto_name = data['conversation']['memory']['crypto']['raw'].upper()

  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
  print(data)
  print(r.json())
  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'The price of {0} is {1} USD or {2} EUR.'.format(crypto_name, r.json()['USD'], r.json()['EUR'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
