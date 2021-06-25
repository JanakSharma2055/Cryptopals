

with open('challenge8.txt') as f:
    encoded_res = [(line.strip()) for line in f]


def has_repeated_blocks(encoded_lines:bytes, blocksize=16):
    if len(encoded_lines) % blocksize != 0:
        raise Exception('ciphertext length is not a multiple of block size')
    else:
        num_blocks = len(encoded_lines) // blocksize
        
    blocks = [encoded_lines[i*blocksize:(i+1)*blocksize] for i in range(num_blocks)]
    #size of blocks will be reduced if it contained repeating elements
    if len(set(blocks)) != num_blocks:
        return True
    else:
        return False


hits = [encoded_line for encoded_line in encoded_res if has_repeated_blocks(encoded_line)]
print(hits)