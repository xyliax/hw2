import hashlib
import re
import sys

re_upper = '[A-Z]'
re_lower = '[a-z]'
re_symbo = '[{}]'.format(re.escape('~`!@#$%^&*()+=_-{}[]\|:;”’?/<>,.'))
re_digit = '[0-9]'

def check(pw):
	if len(pw) < 6:
		return False
	upper = 0 if re.search(re_upper, pw) == None else 1
	lower = 0 if re.search(re_lower, pw) == None else 1
	symbo = 0 if re.search(re_symbo, pw) == None else 1
	digit = 0 if re.search(re_digit, pw) == None else 1
	return upper + lower + symbo + digit >= 3

username = 'bucky'
salt = '0719173488'.encode()
encryptd = 'fdd2a52969ff2cab2c2653e5cc7129a70b0cad398ea3ff44bf700bb0cd\
168d8b5c080c90b9281f04993b05895705229c3a5261e20f8a453369b81efd4f9040b6'


try:
	pw_dict = open('crackstation-human-only.txt', encoding = 'latin-1')
	print('\033[32mCracking...Please wait...\033[0m')
except:
	print('\033[31mYou should download crackstation-human-only.txt first!\033[0m')
	sys.exit(0)

for password in pw_dict.readlines():
	password = password.strip()
	if check(password):
		message = username + ',' + password
		# print(message)
		h = hashlib.scrypt(password = message.encode(), salt = salt, 
				n = 16, r = 32, p = 1)
		if h.hex() == encryptd:
			print(password)

pw_dict.close()

# h = hashlib.scrypt(password = message.encode(), salt = salt.encode(),
#		n = 16, r = 32, p = 1)

# print(h.hex())
