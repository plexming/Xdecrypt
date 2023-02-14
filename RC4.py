from Crypto.Cipher import ARC4 as rc4cipher
import base64


def rc4_algorithm(encrypt_or_decrypt, data, key1):
    if encrypt_or_decrypt == "encrypt":
        key = bytes(key1, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.encrypt(data.encode('utf-8'))
        res = base64.b64encode(res)
        res = str(res,'utf8')
        return res
    elif encrypt_or_decrypt == "decrypt":
        enc = rc4cipher.new(key1)
        res = enc.decrypt(data)
        res = str(res,'utf8')
        return res
