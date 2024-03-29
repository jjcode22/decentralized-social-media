"""
This script will deploy all our contracts
"""

# things to do -
"""
1. deploy Marketplace contract by passing the mint fee to it

Note: make sure you verify the contracts on etherscan while deploying
verifying makes our contracts easily trackable on etherscan
"""
import os
import json
from dotenv import load_dotenv
from brownie import accounts, Marketplace, chain, config
import shutil

load_dotenv()

def clear_development_deployments():
    if chain.id in [1337, '1337', 8545, '8545']:
        deployments_path = "./build/deployments"
        for file in os.listdir(deployments_path):
            try:
                os.remove(f"{deployments_path}/{file}")
            except:
                shutil.rmtree(f"{deployments_path}/{file}")


def store_add_abi(marketplace):
    addresses = json.loads(
        open(
            "../decentralized-social-media-client/constants/addresses.json", "r"
        ).read()
    )
    if not addresses:
        addresses = {}
    addresses[str(chain.id)] = marketplace.address
    with open("../decentralized-social-media-client/constants/abi.json", "w") as abi:
        json.dump(marketplace.abi, abi, indent=3)
    with open(
        "../decentralized-social-media-client/constants/addresses.json", "w"
    ) as add:
        json.dump(addresses, add, indent=3)


def main():
    clear_development_deployments()
    if chain.id in [1337, '1337', 8545, '8545']: 
        Marketplace.deploy((0.0001), {"from": accounts[0]})
    else: 
        account = accounts.add(os.environ.get('PRIVATE_KEY'))
        Marketplace.deploy((0.0001), {"from": account})
    marketplace = Marketplace[-1]
    store_add_abi(marketplace)
