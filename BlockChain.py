from Block import *
import time

class BlockChain():
    DIFFICULTY = 5
    def __init__(self):
        self.chain = []
        self.transactions_pool = []



    def is_valid(self):
        for i in range(1, len(self.chain)):
            last_block = self.chain[i-1]
            current_block = self.chain[i]
            if current_block.hash != current_block.compute_hash():
                print("Block invalid : hash of block is incorrect")
                print(current_block.hash)
                print(current_block.compute_hash())
                return False
            if last_block.hash != current_block.last_hash:
                print("Block are not chained properly")
                return False
            if current_block.hash[:self.DIFFICULTY] != self.string_difficulty():
                print("Block has no proof of work")
                return False
        return True


    def todict(self):
        todict = []
        for block in self.chain:
            todict.append(block.__dict__)
        return todict




    def add_transaction(self, transaction):
        self.transactions_pool.append(transaction)

    def last_block(self):
        return self.chain[-1]

    def hash(self, string):
        return str(hashlib.sha256(str(string).encode()).hexdigest())

    def string_difficulty(self):
        t = ''
        return t.rjust(self.DIFFICULTY, '0')

    def mine(self):
        last_block = self.last_block()
        pool = self.transactions_pool
        nonce = 0
        timestamp = time.time()
        while self.hash(str(last_block.hash) + str(timestamp) + str(Block.todict(pool)) + str(nonce))[:self.DIFFICULTY] != self.string_difficulty():
            nonce = nonce+1
        self.chain.append(Block(last_block.hash, pool, nonce, timestamp))
        return "Mined block !"

    @staticmethod
    def genesis():
        return Block(0, {}, 0, time.time())



