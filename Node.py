import json
from Wallet import *
from flask import Flask
from flask import jsonify
from flask import request
from uuid import uuid4
import requests
from BlockChain import *
from Transaction import *
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = BlockChain()
blockchain.chain.append(blockchain.genesis())
wallet = Wallet(blockchain)

@app.route('/mine', methods=['GET'])
def mine():
    return blockchain.mine()

@app.route('/valid', methods=['GET'])
def valid():
    return jsonify(blockchain.is_valid())

@app.route('/minerate', methods=['POST'])
def minerate():
    request_values = request.get_json()
    amount = request_values["amount"]
    blockchain.set_mining_rate(amount)
    return "Changed mining rate"



@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    request_values = request.get_json()
    print(request)
    print(request_values)
    required = ['sender', 'recipient', 'amount']
    if request_values==None or not all(k in request_values for k in required):
        return 'Missing values', 400
    transaction = Transaction(request_values["sender"], request_values["recipient"], request_values["amount"])
    blockchain.add_transaction(transaction)
    return "Your transaction has been added to the pool"


@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'chain': blockchain.todict(),
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/wallet/balance', methods=['GET'])
def balance():
    return 'Balance :' + wallet.balance()


@app.route('/wallet/newtransaction', methods=['POST'])
def new_transaction_wallet():
    request_values = request.get_json()
    print(request)
    print(request_values)
    required = ['recipient', 'amount']
    if request_values==None or not all(k in request_values for k in required):
        return 'Missing values', 400
    wallet.new_transaction(request_values['amount'], request_values['recipient'])
    return "Your transaction has been added to the pool"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
