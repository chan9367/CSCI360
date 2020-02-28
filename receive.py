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
from Crypto import Random

arguments = sys.argv

if len(arguments) != 4:
    print("Usage:  ./receive <signedmessage> <encryptedmessage> <encryptedsymkey>")
    exit(0)

signedmessage, encryptedmessage, encryptedsymkey = arguments[1],arguments[2],arguments[3]

if not os.path.exists(signedmessage):
    print("signed message file does not exist!")
    exit(0)

if not os.path.exists(encryptedmessage):
    print("encrypted message file does not exist!")
    exit(0)

if not os.path.exists(encryptedsymkey):
    print("encrypted symkey file does not exist!")
    exit(0)
    
ciphertext = open(encryptedsymkey, "rb").read()
    
def RSAdecrypt(ciphertext,privatekey_der):
    key = RSA.importKey(open(privatekey_der,'rb').read())
    #dsize = SHA.digest_size
    #sentinel = Random.new().read(15+dsize)      # Let's assume that average data length is 15
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)
    return message

rsad = RSAdecrypt(ciphertext,"rec_priv.der")
wrsad = open("symkey", "wb")
wrsad.write(rsad)
wrsad.close()

citext = open(encryptedmessage, "rb").read()
key = open("symkey", "rb").read()

def AES_decrypt(ct,key):
    obj = AES.new(key, AES.MODE_CTR,counter=Counter.new(AES.block_size * 8))
    return obj.decrypt(ct)

enct = AES_decrypt(citext,key)
wct = open("msg","wb")
wct.write(enct)
wct.close()

message = open("msg","rb").read()
sig = open(signedmessage, "rb").read()

def verify_sig(message,signature,pubkeyfile_der):
    key = RSA.import_key(open(pubkeyfile_der,'rb').read())
    h = SHA256.new(message)
    verifier = pss.new(key)
    try:
        verifier.verify(h, signature)
        print( "The signature is authentic.")
    except (ValueError, TypeError):
        print( "The signature is not authentic.")

verify_sig(message,sig,"send_pub.der")


