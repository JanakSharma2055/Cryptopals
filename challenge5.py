first_str = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''


def repeating_key_xor(input_str: bytes, key: bytes) -> bytes:
    cipher = b''
    idx = 0
    for byte in input_str:
        cipher+=bytes([byte ^ key[idx]])
        idx = (idx+1) % len(key)
    return cipher.hex()


print(repeating_key_xor(first_str,b'ICE'))
