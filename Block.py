import time
import hashlib

class Block:
    def __init__(self, data, last_hash):
        self.data = data
        self.last_hash = last_hash
        self.timestamp = time.time()
        self.hash = self.compute_hash()



    def compute_hash(self):
        return hashlib.sha3_256(self.data + self.timestamp + self.last_hash)