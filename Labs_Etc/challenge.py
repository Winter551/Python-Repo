encrypted_values = ["0xc", "0x3b", "0x13", "0x2d", "0x23", "0x2a", "0x2f", "0x16", "0x26", "0x39", "0x36"]
key = "ABC"

encrypted_dec_values = []

for i in encrypted_values:
    encrypted_dec_values.append(int(i,16))

print(encrypted_dec_values)

print()

decrypted_values = []
for pos, letter in enumerate(encrypted_dec_values):
    letter_key = key[pos % len(key)]
    decrypted_byte = letter ^ ord(letter_key)
    decrypted_values.append(decrypted_byte)

for i in decrypted_values:
   print(chr(i), end="")