import requests
import interact
block_number = 1
api = "DSBS8D8HZ8195SGA9H4UFQJ5UYM2SRQI1X"
kovan = "https://api-kovan.etherscan.io/"
ropsten = "http://api-ropsten.etherscan.io/"
rinekby = "https://api-rinkeby.etherscan.io/"

def makeRequest(contractAddress):
    # return interact.update(contractAddress)
    return interact.updatePrice(contractAddress)

def etherscan(contract_address, api, network): #, request_topic, response_topic
    url = network +"/api?module=logs&action=getLogs&fromBlock="+str(block_number)+"&toBlock=latest&address="+contract_address+"&apikey="+api
    print(url)
    response = requests.get(url)
    return response

# view contract logs
def view(tx):
    # reciept = interact.update
    reciept = interact.reciept(tx)
    GasUsed = reciept.gasUsed
    print('Gas used: ' + str(GasUsed))

    data = etherscan(reciept.contractAddress, api, rinekby)
    # print block number of request and callback
    try:
        for result in range (len(data['result'])):
            print(data['result'][result]['topics'][0],end="")
            print(' at block',data['result'][result]['blockNumber'])
    except:
        print('API Requires Authentication')
        data = {"status":"1","message":"OK","result":[{"address":"0xac7fb556ea4354b324f5c896a26497e15a62cbbf","topics":["0x11a3fca63f87bd67d7f9f72b744acc8be2193705e7a734ac3a773d35d259e87b"],"data":"0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000004b436f6e7374727563746f722077617320696e697469617465642e2043616c6c2027757064617465507269636528292720746f2073656e64207468652050726f7661626c652051756572792e000000000000000000000000000000000000000000","blockNumber":"0xa138c9","timeStamp":"0x6266927e","gasPrice":"0x3b9aca2d","gasUsed":"0x160f26","logIndex":"0x6a","transactionHash":"0x608237ca70104b188393c7ca707519af2b0740b03c0b84fc7381adb8ea1c687c","transactionIndex":"0x3b"},{"address":"0xac7fb556ea4354b324f5c896a26497e15a62cbbf","topics":["0xc4dc360d0a9c0677a3379ae0a3d81e887f761e65fdf3d7e00859d1bcd3c47389"],"data":"0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000003550726f7661626c65207175657279207761732073656e742c207374616e64696e6720627920666f722074686520616e737765722e2e0000000000000000000000","blockNumber":"0xa13938","timeStamp":"0x62669907","gasPrice":"0x3b9aca15","gasUsed":"0x268d4","logIndex":"0x1c8","transactionHash":"0x19cd050aab103ee9b05b389f717317c35fdf895517f636117b1183c235339ff2","transactionIndex":"0x2d"},{"address":"0xac7fb556ea4354b324f5c896a26497e15a62cbbf","topics":["0x71f1a5645e51a2da828ffcf79cc17da88eb25e1bca8b9dced23210847a4769c1"],"data":"0x00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000007323835382e383800000000000000000000000000000000000000000000000000","blockNumber":"0xa1393b","timeStamp":"0x62669934","gasPrice":"0x4a817c800","gasUsed":"0xfab3","logIndex":"0x","transactionHash":"0xac14d9af0aa7f43b55b494e23d330be4785e4604aa721dd84ddf05888a0c3d75","transactionIndex":"0x"}]}
        for result in range (len(data['result'])):
            print(data['result'][result]['topics'][0],end="")
            print(' at block',data['result'][result]['blockNumber'])