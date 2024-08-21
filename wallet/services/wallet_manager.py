from web3 import Web3
from wallet.config import RPC_URLS

class WalletManager:
    def __init__(self, network="ethereum"):
        self.web3 = Web3(Web3.HTTPProvider(RPC_URLS[network]))

    def get_eth_balance(self, address: str):
        balance = self.web3.eth.get_balance(address)
        return {"balance_wei": balance, "balance_eth": self.web3.fromWei(balance, "ether")}
# 7
# 17
