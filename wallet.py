import subprocess
import json
import bit
import web3
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account
from bit.network import NetworkAPI
import os
from constants import *

load_dotenv()

mnemonic = os.getenv("MNEMONIC", "gown field bottom essence blossom alone mountain panther gain ship memory hurry")



def derive_wallets(mnemonic, coin_type):

    cmd = f"hd-wallet-derive.php -g --mnemonic=\"{mnemonic}\" --cols=path,address,privkey,pubkey --format=json --coin={coin_type} --numderive=3"
    result = subprocess.run(cmd, shell=True, check=True)
    output = result.stdout
    keys = json.loads(output)
    return keys


def extract_data_from_json(json_data):
    return (privKey)

def transact(privKey):
    priv_key_to_account(privKey)
    validate_key(privKey)
    create_tx()
    send_tx()


def validate_key(coin_type, privKey):
    if ETH == coin_type:
        return Account.privateKeyToAccount(priv_key)
    elif BTCTEST == coin_type:
        return PrivateKeyTestnet(priv_key)




if __name__ == "__main__":
    coins = derive_wallets(mnemonic, BTC)
    print(coins)
    # output_json = json.loads(output)
    # return output_json[coin_type]
