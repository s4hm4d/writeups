from Crypto.Cipher import AES

key = "$*#uutCTF*$*3lli0t**Ald3rson*##$"
cipher = open('assets.zip', 'rb').read()

aes = AES.new(key, AES.MODE_ECB)
decrypted = aes.decrypt(cipher)

with open('decrypted.zip', 'wb') as output:
    output.write(decrypted)
