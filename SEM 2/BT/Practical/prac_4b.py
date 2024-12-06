import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    block_info = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(block_info.encode()).hexdigest()

def create_block(index, previous_hash, data):
    timestamp = datetime.datetime.now()
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

# Create a blockchain with a genesis block
blockchain = [Block(0, "0" * 64, datetime.datetime.now(), "Genesis Block",
                    calculate_hash(0, "0" * 64, datetime.datetime.now(), "Genesis Block"))]

# Add a new block to the blockchain
data_for_new_block = "Some data for the new block"
new_block = create_block(len(blockchain), blockchain[-1].hash, data_for_new_block)
blockchain.append(new_block)

# Display the state of the blockchain
for block in blockchain:
    print(f"\nBlock #{block.index} - Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}")