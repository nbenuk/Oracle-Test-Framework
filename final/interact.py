import json
import deploy
import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware

load_dotenv()
node_provider = os.environ['NODE_PROVIDER']

web3_connection = Web3(Web3.HTTPProvider(node_provider))
web3_connection.middleware_onion.inject(geth_poa_middleware, layer=0)

# select and load contract
contract_abi = json.loads(os.environ['CONTRACT_ABI'])

# deploy contract
def delpoy():
    receipt=deploy.deploy_contract()
    return receipt

# get a reciept for a transaction
def reciept(hash):
    return web3_connection.eth.getTransactionReceipt(hash)

# new request for data
def updatePrice(contractAddress):
    ETH = 0.0004

    user = os.environ['ADDRESS_1']
    signature = os.environ['PRIVATE_KEY_1']

    contract = web3_connection.eth.contract(address=contractAddress, abi=contract_abi)
    transaction_body = {
        'nonce':deploy.get_nonce( user),
        'value':web3_connection.toWei(ETH, 'ether')
    }
    function_call = contract.functions.updatePrice().buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(function_call, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result