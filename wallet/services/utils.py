def validate_address(address: str):
    return address.startswith("0x") and len(address) == 42
