import SimpleCrypto as simplecrypto
import pickle
import os.path

class Wallet():
    def __init__(self):
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
