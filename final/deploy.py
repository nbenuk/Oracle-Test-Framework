import os
import json
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
# connect to infura endpoint for testnet
node_provider = os.environ['NODE_PROVIDER']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

def are_we_connected():
    return web3_connection.isConnected()

# smart contract codes loaded
contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_bytecode = os.environ['CONTRACT_BYTECODE']

def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)

def deploy_contract():
    amount_ETH = 0.015
    owner = os.environ['ADDRESS_1']
    signature = os.environ['PRIVATE_KEY_1']
    contract = web3_connection.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    transaction_body = {
        'nonce':get_nonce(owner)+2,
        'value':web3_connection.toWei(amount_ETH, 'ether'),
        'gasPrice': web3_connection.eth.gas_price,
    }
    deployment = contract.constructor().buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(deployment, signature)
    
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)

    receipt = web3_connection.eth.waitForTransactionReceipt(result)
    gasUsed = receipt.gasUsed
    print('gas used ' + str(gasUsed))
    print('contract add ' + str(receipt.contractAddress))

    return receipt
