def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

'''this function takes msg and a key as input and output the xor of msg
and key'''
def xor_single_char_key(msg, key):
    return xor_bytes(msg, bytes([key] * len(msg)))



def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

with open('newfile.txt') as f:
	content = [line.rstrip('\n') for line in f]
	result =[]
	for item in content:
		byte_data =bytes.fromhex(item)
		for i in range(256):
			decoded_text = xor_single_char_key(byte_data, i)
			score =get_english_score(decoded_text)
			result.append((score,decoded_text, chr(i)))

	for flag in sorted(result, key= lambda x: x[0],reverse=True)[:10]:
		print(flag)


