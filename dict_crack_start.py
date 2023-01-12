# Script:  dict_crack_start.py
# Description: Cracks password hash using a dictionary attack.
#              And find md5 hashes from a webpage
# Author:  
# Modified: 07/12/2018
import sys
import hashlib
import re

# list of passwords



def dict_attack(passwd_hash):
    """Checks password hash against a dictionary of common passwords"""

    dic = ['123','1234','12345','123456','1234567','12345678',
        'password', 'qwerty','abc','abcd','abc123','111111',
        'monkey','arsenal','letmein','trustno1','dragon',
        'baseball','superman','iloveyou','starwars',
        'montypython','cheese','123123','football','batman']

# create list of corresponding md5 hashes using a list comprehension
    hashes = [hashlib.md5(pwd.encode('utf-8')).hexdigest() for pwd in dic] 
# zip dic and hashes to create a dictionary (rainbow table)
    rainbow = dict(zip(hashes, dic)) 


    dicUP = []
    for up in dic:
        dicUP.append(up.upper())
    hashesUP = [hashlib.md5(pwd.encode("utf-8")).hexdigest() for pwd in dicUP]
    rainbowUP = dict(zip(hashesUP, dicUP))

    dicIUP = []
    for iup in dic:
        dicIUP.append(iup.capitalize())
    hashesIUP = [hashlib.md5(pwd.encode("utf-8")).hexdigest() for pwd in dicIUP]
    rainbowIUP = dict(zip(hashesIUP, dicIUP))

    #print (f'[*] Cracking hash: {passwd_hash}')

    passwd_found = rainbow.get(passwd_hash)
    passwd1_found = rainbowUP.get(passwd_hash)
    passwd2_found = rainbowIUP.get(passwd_hash)
    if passwd_found:
        print (f'[*] Cracking hash: {passwd_hash} [+] Password recovered: {passwd_found}')
    elif passwd1_found:
        print (f'[*] Cracking hash: {passwd_hash} [+] Password recovered: {passwd1_found}')
    elif passwd2_found:
        print (f'[*] Cracking hash: {passwd_hash} [+] Password recovered: {passwd1_found}')
        #print(rainbowIUP)
    else:
        print (f'[*] Cracking hash: {passwd_hash} [-] no matching password found')

def findhashes(page):
    ''' Extract all md5 hashes from a webpage '''

    #regex to get md5 hashes
    passwd = re.findall('[a-z0-9]{32}', page)
    for x in passwd:
        dict_attack(x)
                
def main():
    print('[dict_crack] Tests')
    if len(sys.argv)==1:
        sys.argv.append('0d107d09f5bbe40cade3de5c71e9e9b7')
    dict_attack(sys.argv[1])
    
if __name__ == '__main__':
	main()
