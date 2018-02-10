#!/usr/bin/python
# coding:utf-8

# yyets - restore.py
# 2018/2/9 19:58
# 

author = 'Benny <benny@bennythink.com>'

import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt(data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()


def process(filename, key):
    raw_file = open(filename, 'rb')
    final_file = open('%s_decrypt.mp4' % filename.split('.')[0], 'wb')
    data = 1
    while data:
        data = raw_file.read(16)
        final_file.write(decrypt(data, key))
        data = raw_file.read(4080)
        final_file.write(data)

    raw_file.close()
    final_file.close()


def get_aes_key(file_id):
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    if sys.version > '3':
        digest.update((file_id + 'zm' + file_id).encode('utf-8'))
    else:
        digest.update(file_id + 'zm' + file_id)

    return digest.finalize()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python yyets.py sample.mp4 fb755fd1b51c769bfed987e2a8c8b03ee7a8e7cc')
    else:
        aes_key = get_aes_key(sys.argv[2])
        process(sys.argv[1], aes_key)
