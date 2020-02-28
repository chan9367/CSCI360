#! /usr/bin/python3


import hashlib
import sys
import os
from Crypto.Cipher import AES
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA
from Crypto.Util import Counter

arguments = sys.argv

if len(arguments) != 4:
    print("Usage:  ./send <messagefile> <senderprivkey> <receiverpubkey>")
    exit(0)

messagefile, senderprivkey, receiverpubkey = arguments[1],arguments[2],arguments[3]

if not os.path.exists(messagefile):
    print("message file does not exist!")
    exit(0)

if not os.path.exists(senderprivkey):
    print("sender private key file does not exist!")
    exit(0)

if not os.path.exists(receiverpubkey):
    print("receiver public key file does not exist!")
    exit(0)
    

message = open(messagefile, "rb").read()

def sign_message(message,privkeyfile_der):
        key = RSA.import_key(open(privkeyfile_der,'rb').read())
        h = SHA256.new(message)
        signature = pss.new(key).sign(h)
        return signature
    
sig = sign_message(message,senderprivkey)    
signame = open("msg.sig", "wb")
signame.write(sig)
signame.close()
    
key = open("symkey","rb").read()
message = open(messagefile, "rb").read()

def AES_encrypt(msg, key):
        obj = AES.new(key, AES.MODE_CTR,counter=Counter.new(AES.block_size * 8))
        return obj.encrypt(msg)
        
ck = AES_encrypt(message, key)
wck = open("msg.crypt", "wb")
wck.write(ck)
wck.close()
        
def RSAencrypt(message,pubkeyfile_der):
        key = RSA.importKey(open(pubkeyfile_der,'rb').read())
        cipher = PKCS1_OAEP.new(key)  ### Padding Scheme
        ciphertext = cipher.encrypt(message)
        return ciphertext
        
ciphertext = RSAencrypt(key,receiverpubkey)
wct = open("symkey.crypt", "wb")
wct.write(ciphertext)
wct.close()

