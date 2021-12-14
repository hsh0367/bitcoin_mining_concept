from hashlib import sha256
import time


MAX_NONCE = int(1e10)
DIFFICULTY = 5

# use Block 714140
# https://www.blockchain.com/btc/block/00000000000000000005f294a7debd10e2c0f8d39d1dbe0fe8a9daf84103110d
block_number = 714140
# dummy transaction
transactions = """
    {
        "txid": "263c018582731ff54dc72c7d67e858c002ae298835501d\
                  80200f05753de0edf0",
        "vout": 0,
        "address": "muhtvdmsnbQEPFuEmxcChX58fGvXaaUoVt",
        "scriptPubKey": "76a9149ba386253ea698158b6d34802bb9b550\
                          f5ce36dd88ac",
        "amount": 40.00000000,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
    },
    {
        "txid": "263c018582731ff54dc72c7d67e858c002ae298835501d\
                  80200f05753de0edf0",
        "vout": 1,
        "address": "mvbnrCX3bg1cDRUu8pkecrvP6vQkSLDSou",
        "account": "",
        "scriptPubKey": "76a914a57414e5ffae9ef5074bacbe10a320bb\
                          2614e1f388ac",
        "amount": 10.00000000,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
    }
"""
prev_hash = "00000000000000000005f294a7debd10e2c0f8d39d1dbe0fe8a9daf84103110d"

new_hash = None

start_time = time.time()

for nonce in range(MAX_NONCE):
    text = str(block_number) + transactions + prev_hash + str(nonce)
    new_hash = sha256(text.encode("ascii")).hexdigest()

    if new_hash.startswith("0" * DIFFICULTY):
        # Mining Success
        print(f"Hash: {new_hash}")
        print(f"Nonce: {nonce}")
        break

if new_hash is None:
    print("Mining failed.")

print(f"Mining time {time.time() - start_time}s!")
