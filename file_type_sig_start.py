# Script: file_type_sig_start.py
# Desc:   Check file type signature against filename extension.
# Author: Mohammed Almouhanna
# Modifed: 07/12/2018
#
import sys
import os
import binascii

file_sigs = {b'\xFF\xD8\xFF': ('JPEG', 'jpg'), b'\x47\x49\x46': ('GIF', 'gif'),
             b'\x25\x50\x44': ('pdf', 'PDF'), b'\x50\x4B\x03': ('docx', 'DOCX')}


def check_sig(filename):
    """checks the file type signature of the file passed in as arg,
    returning the type of file and correct extension in a tuple """

    # Read File
    f = open(filename,'rb')
    file_sig = f.read(3)
    print('[*] check_sig() File:', filename, end=' ')
    print('Hash Sig:', binascii.hexlify(file_sig))

    # Check for file type sig
    if file_sig not in file_sigs:
        print('[-] File type not identified - file sig not in db\n')
        return (-1,'','')


    # File Type Sig found, so get sig and ext from file_sigs dic
    file_type = file_sigs[file_sig]
    file_ext = file_type[0]
    if file_ext != file_type:
        print(f'[+] File type identified as {file_type[0]}')
        print(f'[+] Extension: {os.path.splitext(filename)[1]}')
        print(f'[!] Expected : {file_ext}. Investigation recommended.\n')
        return (-2,file_type,file_ext)


    # Check if Type matches valid file extension
    if file_sig == file_sigs[file_sig]:
        print(f'[+] File type identified as {file_type}')
        print('[+] Extension:', os.path.splitext(filename)[1])
        print('[ ] OK - valid extension for this file type')
        return (0,file_type,file_ext)
    


def main():
    # temp testing url argument
    sys.argv.append(os.getcwd())

    # Check args
    if len(sys.argv) != 2:
        print('usage: file_sig filename')
        sys.exit(1)

    file_hashsig = check_sig('icon_clown.gif')


if __name__ == '__main__':
    main()
