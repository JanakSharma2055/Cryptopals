def pad(text, size):
    """pads text to make it of size `size`,
    according to the PKCS#7 padding scheme

    Args:
        text (bytes): the text to pad
        size (int): required size of padded string

    Returns:
        bytes: the padded string with size = `size`
    """
    length = len(text)
    if length % size == 0:
        return text
    
    padding = size - (length % size)
    padValue = hex(padding).lstrip('0x')
    if len(padValue) == 1:
        padValue = '0' + padValue # bytes can't convert single digit hex
    padValue = bytes.fromhex(padValue)

    paddedString = text + padValue * padding

    return paddedString

given = b'YELLOW SUBMARINE'
requiredLength = 20 # say
paddedString = pad(given, requiredLength)
print(paddedString)