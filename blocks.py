# initialize a block. Note 'transactions' is initialized as an empty list
block = {
    'height':1,
    'time':0,
    'prevHash':'this is the genesis block',
    'merkleRoot': '',
    'transactions': []
        }
print(block)

# create a transaction, in this case a string
transaction='Pay $1,000,000 to Jeff'
print(transaction)

encoded_tx = transaction.encode()
print(encoded_tx)

import hashlib as hash

hashed_tx = hash.sha1(encoded_tx)
print(hashed_tx)

hex_tx = hashed_tx.hexdigest()
block["transactions"].append(hex_tx)
print(block)

# some attributes have been hard-coded for simplicity
block2 = {
    'height':2,
    'time':1,
    'prevHash':'null',
    'merkleRoot': 'null',
    'transactions': []
        }
# create a transaction and add it to the block
tx = hash.sha1('Alice +10'.encode()).hexdigest()
block2["transactions"].append(tx)
block2["merkleRoot"] = tx
print(block2)

import pickle
# convert to a byte object
byte_genesis = pickle.dumps(block)
print(byte_genesis)

# compress to a human-readable SHA-1 digest
hash_genesis = hash.sha1(byte_genesis).hexdigest()
print('\n')
print(hash_genesis)

# set the prevHash and print the block
block2["prevHash"] = hash_genesis
for key, value in block2.items():
    print(key+': '+str(value)) 