def find_hamming_distance(string1: bytes, string2: bytes) -> int:
    """
    Find hamming distance between two strings.
    The Hamming distance is just the number of differing bits.

    :param string1: The first string to be compared, as bytes
    :param string2: The second string to be compared, as bytes
    :returns: The hamming distance between the two params as an int
    """
    distance = 0
    for byte1, byte2 in zip(string1, string2):
        diff = byte1 ^ byte2
        # XOR only returns 1 if bits are different
        distance += sum([1 for bit in bin(diff) if bit == '1'])
    return distance