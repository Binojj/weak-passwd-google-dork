text = "an0n4ce{dc8ffb5750fdf0eee89fa1e6af55acda}"

def encrypt(text,key):
    encrypted_txt = ''
    hex_enc_txt = ''
    for i in range(0,len(text)):
        xored = ord(text[i]) ^ ord(key)
        encrypted_txt +=  chr(xored)
        hex_enc_txt += hex(xored) + '-'
    li = list(hex_enc_txt)
    li.pop()
    hex_enc_txt = ''.join(li)
    return encrypted_txt,hex_enc_txt


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in alpha:
    ciphered_txt,cip_hex = encrypt(text, 'Q')

    # print(ciphered_txt)
    print(cip_hex)

    deciphered_txt = decrypt(ciphered_txt, i)
    print(deciphered_txt)
