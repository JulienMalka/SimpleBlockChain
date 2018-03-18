import json
from flask import Flask
from flask import jsonify
from uuid import uuid4
from BlockChain import *
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = BlockChain()
blockchain.chain.append(blockchain.genesis())


@app.route('/mine', methods=['GET'])
def mine():
    return blockchain.mine()

@app.route('/valid', methods=['GET'])
def valid():
    return jsonify(blockchain.is_valid())



@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.todict(),
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)