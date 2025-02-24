import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")

#To Encrypt

text = input("Enter the message to encrypt: ")
cipher_code = ""

for letter in text:
    index = chars.index(letter)
    cipher_code += key[index]

print(f"Original message : {text}")
print(f"Encrypted message: {cipher_code}")


#To Decrypt

cipher_code = input("Enter the message to Decrypt: ")
text = ""

for letter in cipher_code:
    index = key.index(letter)
    text += chars[index]


print(f"Encrypted message: {cipher_code}")
print(f"Original message : {text}")
