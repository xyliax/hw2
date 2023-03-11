# usr/bin/env python3

'''
CS642 HW2
Group HW2 19 ypei23 vjanarthanan

How to run: 'python3 pwcrack.py'
This program cracks the two users specified in the tasks.
If you want to crack other's, modify line 26, 27, 28.

After at least 1 passwords are found for all users, the program will stop
and ask whether you want to continue and find more possibilities.
Due to the property of hash functions, there is a very small chance to 
have different passwords mapped to the same text.

Output format: several lines in red, each line is [username] -> [password]
'''


import hashlib
from itertools import product
import time

pw_list = ['2', '0', '3', '6', '1', '5', '4', '7', '8', '9', ''];

user = ['bjacobsen', 'ceccio']
salt = ['980166', '547750']
encr = ['ffa2dcdd84a45582b17d4f535cda63887273f34a679eded10428b480999c3a8b',
        '41db4f70c8ce1c866462b4c0636aef38c1ea5ef36809bf099165c826bc3a8881']

prompt = '''\033[32m
All users\' passwords are cracked! (At least once)
Theoretically there may exist other possible passwords.
But it may cost longer to try all possibilities.
Type \'more\' to Find More, or Quit[ENTER]:\033[0m'''

def crack(user, salt, encr, n):
    flag = [False] * n
    cracked = 0
    for p in product(pw_list, repeat = 8): 
        guess = ''.join(p)
        for k in range(n):
            res = f'{user[k]},{guess},{salt[k]}'
            rl = hashlib.sha256(res.encode()).hexdigest()
            if rl == encr[k]:
                print('\033[31m' + user[k] + ' -> ' + guess + '\033[0m')
                if flag[k] == False:
                    flag[k] = True
                    cracked += 1
                if cracked == n and input(prompt) != 'more':
                    return

crack(user, salt, encr, 2)

