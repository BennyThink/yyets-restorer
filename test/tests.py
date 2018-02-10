#!/usr/bin/python
# coding:utf-8

# yyets-yyets - tests.py.py
# 2018/2/10 16:42
# 

author = 'Benny <benny@bennythink.com>'
import os
import sys
from binascii import hexlify
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

sys.path.append(os.getcwd())
from yyets import restore

KEY = '3106f82032ab5f9a2a4047ac671a39f5'
DECRYPT_DATA = '000000146674797069736f6d00000001'
HASH = '85bc2dd615df1d599262e966fbeee675d75dd7966871f56702cd10d39f6f8efb'


def key_test(_file_id):
    aes_key = restore.get_aes_key(_file_id)

    if sys.version > '3':
        assert str(hexlify(aes_key))[2:-1] == KEY
    else:
        assert hexlify(aes_key) == KEY
    return aes_key


def decrypt_test(_file_id):
    key = key_test(_file_id)
    raw_file = open('yyets/sample.mp4', 'rb')

    if sys.version > '3':
        assert DECRYPT_DATA == str(hexlify(restore.decrypt(raw_file.read(16), key)))[2:-1]
    else:
        assert DECRYPT_DATA == hexlify(restore.decrypt(raw_file.read(16), key))
    raw_file.close()


def hash_test():
    os.system('python yyets/restore.py yyets/sample.mp4 fb755fd1b51c769bfed987e2a8c8b03ee7a8e7cc')
    raw_file = open('yyets/sample_decrypt.mp4', 'rb')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(raw_file.read())

    if sys.version > '3':
        assert str(hexlify(digest.finalize()))[2:-1] == HASH
    else:
        assert hexlify(digest.finalize()) == HASH
    raw_file.close()

    os.remove('yyets/sample_decrypt.mp4')


if __name__ == '__main__':
    file_id = 'fb755fd1b51c769bfed987e2a8c8b03ee7a8e7cc'
    key_test(file_id)
    decrypt_test(file_id)
    hash_test()
