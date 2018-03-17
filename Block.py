import time
import hashlib

class Block:
    def __init__(self, index, data, last_hash):
        self.index = index
        self.data = data
        self.timestamp = time.time()
        self.last_hash = last_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        to_be_hashed = str(self.index) + str(self.last_hash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(to_be_hashed.encode()).hexdigest()


    @staticmethod
    def genesis():
        return Block(0, "genesis", None)



