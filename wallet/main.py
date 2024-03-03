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
# 12
# 28
# 38
# 40
# 47
# 59
# 60
# 63
# 68
# 72
# 76
# 80
# 81
# 82
# 90
# 91
# 92
# 100
# 101
# 105
# 106
# 115
# 116
# 119
# 127
# 138
# 148
# 149
# 153
# 155
# 157
# 161
# 167
# 172
# 174
# 177
# 178
# 182
# 188
# 194
# 195
# 204
# 209
# 210
# 215
# 218
# 227
# 233
# 235
# 256
# 269
# 276
# 278
# 282
# 283
# 292
# 294
# 311
# 319
# 324
# 326
# 331
# 332
# 339
# 340
# 341
# 345
# 354
# 358
# 367
# 369
# 370
# 373
# 379
# 382
# 387
# 393
# 401
# 402
# 413
# 421
# 423
# 426
# 427
# 430
# 434
# 441
# 442
# 456
# 467
# 475
# 486
# 488
# 491
