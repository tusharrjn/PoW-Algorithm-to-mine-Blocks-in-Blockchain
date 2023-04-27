import hashlib
import time

class Block:
    def __init__(self, prev_hash, data, filecoin_difficulty):
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = time.time()
        self.nonce = 0
        self.filecoin_difficulty = filecoin_difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = str(self.prev_hash) + str(self.data) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mine_block(self):
        filecoin_target = 2 ** (256 - self.filecoin_difficulty)
        while int(self.hash, 16) >= filecoin_target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined:", self.hash)

class Blockchain:
    def __init__(self, difficulty, filecoin_difficulty):
        self.difficulty = difficulty
        self.filecoin_difficulty = filecoin_difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0", "Genesis Block", self.filecoin_difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.prev_hash = self.get_latest_block().hash
        new_block.mine_block()
        self.chain.append(new_block)

if __name__ == '__main__':
    blockchain = Blockchain(2, 20)
    block1 = Block("", "Transaction Data 1", blockchain.filecoin_difficulty)
    blockchain.add_block(block1)
    block2 = Block("", "Transaction Data 2", blockchain.filecoin_difficulty)
    blockchain.add_block(block2)
