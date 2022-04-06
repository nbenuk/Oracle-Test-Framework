from urllib import response
import requests
block_number = 10457773
addresss = "0x40228bEf42e300e587ECdE28aFA6808F3B56C0Cc"
api = "DSBS8D8HZ8195SGA9H4UFQJ5UYM2SRQI1X"

url = "https://api-rinkeby.etherscan.io/api?module=logs&action=getLogs&fromBlock="+ str(block_number) +"&toBlock=latest&address="+addresss+"&topic0=0x71f1a5645e51a2da828ffcf79cc17da88eb25e1bca8b9dced23210847a4769c1&apikey="+api
print(url)
response = requests.get(url)
with open('output.html', 'w') as f:
    f.write(response.text)
# print(response.content)
