import web3
import base64
import binascii
import pandas as pd
import time

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# TESTED WITH python 3.6

# Fill these in to test, ex. remove @RPC_ENDPOINT@
USER = "xxx"
PASS = "xxx"
RPC_ENDPOINT = "https://xxxx-rpc.de0-aws.kaleido.io"

# Encode the username and password from the app creds into USER:PASS base64 encoded string
auth = USER + ":" + PASS
encodedAuth = base64.b64encode(auth.encode('ascii')).decode('ascii')

# Build the header object with the Basic auth and the standard headers
headers = {'headers': {'Authorization': 'Basic %s' % encodedAuth,
                       'Content-Type': 'application/json',
                       'User-Agent': 'kaleido-web3py'}}

# Construct a Web3 object by constructing and passing the HTTP Provider
provider = HTTPProvider(endpoint_uri=RPC_ENDPOINT, request_kwargs=headers)
w3 = Web3(provider)


# Add the Geth POA middleware needed for ExtraData Header size discrepancies between consensus algorithms
# See: http://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority
# ONLY for GETH/POA; If you are using quorum, comment out the line below
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

# Get the latest block in the chain
# block = w3.eth.getBlock("latest")

# Print the block out to the console
# print(block)

address = w3.eth.accounts
address = str(address)
print(address)
address = address[2:-2]

balance = w3.eth.getBalance(address)

contract_add = w3.toChecksumAddress('0x7b74e8c563c1fbcff30ecc8869a5e3f7acf17906')

print(balance)

myContract = w3.eth.contract(address=contract_add)

print(myContract)

tweet = pd.read_csv("blockchain-022120.csv")

number_tweet = len(tweet) 

i=0

while  i < number_tweet:

        tweet_link=str(tweet.at[i,'Text'])
        tweet_score=str(tweet.at[i,'Score'])
        #tweet_string = tweet_link.to_string(header=False,
        #          index=i).split('\n')
        tweet_string = tweet_link.encode('utf-8') + '  SCORE = '.encode('utf-8') + tweet_score.encode('utf-8')
        hex_link = tweet_string.hex()
        print(hex_link)

        w3.eth.sendTransaction({'to': contract_add, 'from':address, 'gas':1000000, 'data':hex_link})
        print(i,'registrato !')

        time.sleep(5)
        i  += 1


