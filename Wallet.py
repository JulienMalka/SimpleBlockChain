import SimpleCrypto as simplecrypto
from Transaction import *
import pickle
import os.path

class Wallet():
    def __init__(self, blockchain):
        self.blockchain = blockchain
        if os.path.exists('wallet.pkl'):
            pkl_file = open('wallet.pkl', 'rb')
            keys = pickle.load(pkl_file)
            pkl_file.close()
            self.private_key = keys['private']
            self.public_key = keys['public']
        else:
            self.public_key, self.private_key = simplecrypto.generate_keypair()
            keys = {'public' : self.public_key, 'private' : self.private_key}
            output = open('wallet.pkl', 'wb')
            pickle.dump(keys, output)
            output.close()

        print("Public key : "+str(self.public_key))
        print("Private key (keep that safe) : " + str(self.private_key))

    def balance(self):
        balance = 0
        for block in self.blockchain.chain:
            for transaction in block.transactions:
                print(transaction)
                if transaction['sender'] == self.public_key:
                    balance = balance - transaction['amount']
                if transaction['recipient'] == self.public_key:
                    balance = balance + transaction['amount']
        return balance


    def new_transaction(self, recipient, amount):
        transaction_unsigned = Transaction(self.public_key, recipient, amount, None)
        to_sign = transaction_unsigned.dump()
        signature = simplecrypto.encrypt(self.private_key, to_sign)
        transaction_unsigned.sign_transaction(signature)
        transaction_signed = transaction_unsigned
        if transaction_signed.is_valid():
            self.blockchain.add_transaction(transaction_signed)
            print("transaction valid -> added to pool")
        else:
            print("something went wrong")
