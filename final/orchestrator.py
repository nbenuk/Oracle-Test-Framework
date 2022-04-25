import test
import interact
import deploy
receipt=deploy.deploy_contract()
result = interact.updatePrice(receipt.contractAddress)
test.view(receipt.transactionHash)