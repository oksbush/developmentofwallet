from fastapi import FastAPI
from wallet.services.wallet_manager import WalletManager
from wallet.services.token_swap import swap_tokens
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crypto Wallet API"}

@app.get("/balance/{address}")
def get_balance(address: str):
    manager = WalletManager()
    return manager.get_eth_balance(address)
# 1
# 3
# 5
# 9
# 11
