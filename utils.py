def xor_checksum(data: bytes) -> int:
    checksum: int = 0
    for char in data:
        checksum ^= char
    return checksum
