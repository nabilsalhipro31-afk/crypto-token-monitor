from web3 import Web3
import time

RPC_URL = "https://rpc.ankr.com/eth"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def scan_block():
    latest_block = w3.eth.block_number
    block = w3.eth.get_block(latest_block, full_transactions=True)

    for tx in block.transactions:
        if tx.to is None:
            print("New contract detected:", tx.hash.hex())

def main():
    print("Monitoring blockchain...")
    while True:
        scan_block()
        time.sleep(5)

if __name__ == "__main__":
    main()
