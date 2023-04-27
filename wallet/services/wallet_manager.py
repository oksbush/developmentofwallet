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
# 23
# 33
# 35
# 39
# 48
# 55
# 61
# 69
# 71
# 75
# 85
# 88
# 96
# 108
# 109
# 110
# 111
# 128
# 132
# 133
# 135
# 141
# 145
# 146
# 154
# 156
# 159
# 160
# 164
# 166
# 171
# 173
# 179
# 180
# 181
# 191
# 201
# 205
# 208
# 213
# 214
# 219
# 220
# 223
# 228
# 232
# 234
# 240
# 241
# 242
# 243
# 244
