
# lib_crypt.py		written by Duncan Murray 1/5/2014
# functions for various ciphers, encryptions, translators

"""
010000100110010100100000011100110111010101110010011001
010010000001110100011011110010000001100100011100100110
100101101110011010110010000001111001011011110111010101
110010001000000100111101110110011000010110110001110100
01101001011011100110010100101110


"""

import random
import math
import binascii

try:
	from Crypto.Cipher import AES
except:
	print('You need to install https://pypi.python.org/pypi/pycrypto/2.6.1')

def TEST():
	print('lib_crypt.py - misc functions for ciphers, encryptions, translators')
	ASCII_chart()
	txt = 'hi there'
	test_base64(txt)
	test_crypto(txt)

def test_base64(msg):
	bin = txt2bin(msg)
	print('encoding base 64 : ' + msg + '\nbin = ' + bin)
	reCoded = bin2txt(bin)
	print('decoding base 64 : ' + reCoded)
	
def test_crypto(msg):
	try:
		secret = encrypt_AES('key123', msg, 'iv456')
		result = decrypt_AES('key123', secret, 'iv456')
		print()
		print('original  = ' + msg)
		print('encrypted = ' + secret)
		print('decrypted = ' + result)
	except:
		print('encryption test failed')

	
def encode64(visible_text): return base64.b64encode(bytes(visible_text, 'utf-8')).decode('utf-8')
def decode64(poorly_hidden_text): return base64.b64decode(poorly_hidden_text).decode('utf-8')


def encrypt_AES(key, plain_text, IV456):
	obj = AES.new(key, AES.MODE_CBC, IV456)
	return obj.encrypt(plain_text)
	
def decrypt_AEX(key, ciphertext, IV456):	
    obj = AES.new(key, AES.MODE_CBC, IV456)
    return obj.decrypt(ciphertext)

	
	
def txt2bin(txt): 
	#The code expects ascii characters in range: [ -~]
	return bin(int(binascii.hexlify(txt.encode('ascii', 'strict')), 16))

def bin2txt(bin):
	n = int(bin, 2)
	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()	


def test_full_range():
	for i in range(0, 128):
		char = chr(i)
		print(str(i) + '  ' + char + ' ' + txt2bin(char))

def pprint_binary(txt):
	op = txt[2:].zfill(7)
	return op[:4] + '-' + op[4:]
		
def ASCII_chart():
	rows = 32
	cols = 4
	chars = []
	for i in range(0, 204):
		if i < 128:
			chars.append(str(i).zfill(3) + ' ' + pprint_binary(txt2bin(chr(i))) + ' ' + chr(i).zfill(1) )
			matrix = [['     ' for z in range(0, cols)] for z in range(0, rows)] 
	for y in range(0, rows):
		for x in range(0,cols):
			#print (x,y,i)
			matrix[y][x] = chars[((y*(cols))+x)]
	
	txt = ''
	for rowList in matrix:
		for col in rowList:
			txt += col + '  '
		print(txt)
		txt = ''

	
if __name__ == '__main__':
    TEST()	
	

