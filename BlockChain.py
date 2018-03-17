from Block import *

class BlockChain(object):
    DIFFICULTY = 5
    def __init__(self):
        self.chain = []




    def is_valid(self):
        for i in range(1, len(self.chain)):
            last_block = self.chain[i-1]
            current_block = self.chain[i]
            if current_block.hash != current_block.compute_hash:
                return False
            if last_block.hash != current_block.last_hash:
                return False
            if current_block.hash[:self.DIFFICULTY]!= [0]*self.DIFFICULTY:
                return False
            if current_block.index != last_block.index +1:
                return False
        return True











