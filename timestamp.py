import hashlib as hash
import pickle
import time

class Block:
    def __init__(self, prev_hash, timestamp, merkle_root, transactions):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.transactions = transactions

    def calculate_hash(self):
        byte_self = pickle.dumps(self)
        return hash.sha1(byte_self).hexdigest()
    
genesis_block = Block('this is the genesis block', time.time(), '', [])
gen_hash = genesis_block.calculate_hash();
print(gen_hash);
print(time.time())

block_2 = Block(gen_hash, time.time(), '', [])
print("block 2" + block_2.calculate_hash())


#Block height makes it very easy to traverse the blockchain, and reference a specific block.
#Timestamp is the time the block was created, which makes it easy to determine when the block was created.
#timestamps help to detect the order in which blocks were created.
