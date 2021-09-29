# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
from web3 import Web3
from eth_account import Account
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.auto.gethdev import w3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
 
#Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
   
    keys = json.loads(output)
    return  keys

# Test the function derive_wallets
derive_wallets(mnemonic, 'BTC', 3)

#Setting dictionary of coins to be used in the wallet
coins = {"eth", "btc-test", "btc"}
numderive = 3

keys = {}
for coin in coins:
    keys[coin]= derive_wallets(mnemonic, coin, numderive=3)
    
# Key for testing transactions (First address for both ETH and BTC-Test)
eth_PrivateKey = keys["eth"][0]['privkey']
btc_PrivateKey = keys['btc-test'][0]['privkey']

# Derive the wallet keys
print(json.dumps(keys, indent=4, sort_keys=True))

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to":recipient, "value": amount})
        return {
            "from": account.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)}
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, recipient, amount):
    tx = create_tx(coin, account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH: 
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    elif coin == BTCTEST: 
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
    
# Test account
btc_acc = priv_key_to_account(BTCTEST, btc_PrivateKey)

# Transfer to another BTC Test address
send_tx(BTCTEST,btc_acc,"mkdm9urvx4WxNDFDytNQ142WQdgmc66szp", 0.000002)

