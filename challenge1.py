#will work on this later--------------------------
# # print(bytes.fromhex(res))
# str1='1c0111001f010100061a024b53535009181c'
# str2 ='686974207468652062756c6c277320657965'

# def do_xor(xs, ys):	
# 	return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
	
# res =do_xor(str1,str2)
# for x in res:
# 	print(ord(x),end="")

# def xor_bytes(a, b):
#     return bytes([x ^ y for x, y in zip(a, b)])

# '''this function takes msg and a key as input and output the xor of msg
# and key'''
# def xor_single_char_key(msg, key):
#     return xor_bytes(msg, bytes([key] * len(msg)))


# given_str =bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

# for i in range(255):
# 	print(xor_single_char_key(given_str,i))