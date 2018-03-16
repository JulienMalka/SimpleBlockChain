import time
import hashlib

class Block:
    def __init__(self, data, last_hash):
        self.data = data
        self.last_hash = last_hash
        self.timestamp = time.time()
        self.hash = self.compute_hash()



    def compute_hash(self):
        return hashlib.sha256((str(self.timestamp)+str(self.data)+str(self.last_hash)).encode()).hexdigest()



