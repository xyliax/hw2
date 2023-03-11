# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16 + 16 + 32:
    print("Ciphertext is too short!")
    sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

message = \
"""AMOUNT: $  12.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""

real_amount = 'AMOUNT: $  12.99'
fake_amount = 'AMOUNT: $9999999'

A = int(real_amount.encode().hex(), 16)
B = int(fake_amount.encode().hex(), 16)

mod_iv = A ^ B ^ int(iv.hex(), 16) 
mod_message = message.replace(real_amount, fake_amount)
mod_tag = hashlib.sha256(mod_message.encode()).hexdigest()

mod_text = hex(mod_iv)[2:] + ciphertext[16:].hex() + mod_tag
print(mod_text)

