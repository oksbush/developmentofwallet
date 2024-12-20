from pydantic import BaseModel

class SwapRequest(BaseModel):
    from_token: str
    to_token: str
    amount: float
# 2
