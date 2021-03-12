import subprocess
import json

import os
from constants import *

mnemonic = os.getenv("MNEMONIC", "gown field bottom essence blossom alone mountain panther gain ship memory hurry")



def derive_wallets(mnemonic, coin_type):

    p = subprocess.Popen(["echo", "$SHELL"], stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    print(out)

    # p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
    # out, err = p.communicate()
    # print(out)

    cmd = "echo"
    args = "$SHELL"

    # cmd = "hd-wallet-derive.php"
    # args = f"-g --mnemonic=\"{mnemonic}\" --cols=path,address,privkey,pubkey --format=json --coin={coin_type} --numderive=3"

    # command = [ "hd-wallet-derive.php", "-g", f"--mnemonic={mnemonic}", "--cols=path,address,privkey,pubkey", "--format=json}", f"--coin={coin_type}", "--numderive=3" ]
    # command = f"hd-wallet-derive.php -g --mnemonic={mnemonic} --cols=path,address,privkey,pubkey --format=json --coin={coin_type} --numderive=3"
    p = subprocess.Popen(args=args, executable=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # str(os.getcwd())
    # cur_dir + "/hd-wallet-derive.php ~~~"
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # (stdout, stderr) = p.communicate()

    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    print(keys)

    output_json = json.loads(output)
    return output_json[coin_type]

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
    import subprocess
    coins = derive_wallets(mnemonic, ETH)
