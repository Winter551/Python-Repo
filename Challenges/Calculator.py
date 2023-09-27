x = input("Pick a number: ")
y = input("Pick another number: ")
z = input("Pick an operator: ")

if z == ("*"):
    print(int(x) * int(y))
if z == ("/"):
    print(int(x) / int(y))
if z == ("+"):
    print(int(x) + int(y))
if z == ("-"):
    print(int(x) - int(y))


def xor_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        plaintext += decrypted_char
    return plaintext

ciphertext = "$/8#$!%&&$:;/.8\"%.%#%#"

print("Brute-forcing 1-byte XOR decryption:")
for key in range(256):
    decrypted_text = xor_decrypt(ciphertext, key)
    print(f"Key: {key:02X} - Decrypted Text: {decrypted_text}")
