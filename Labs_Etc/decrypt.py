hex_encrypted = ['0x11', '0x03', '0x10', '0x17', '0x12']

xor_key = "PASSW"

encrypted_dec_values = []

for i in hex_encrypted:
    encrypted_dec_values.append(int(i,16))
print(encrypted_dec_values)

decrypted_values = []

for pos, val in enumerate(encrypted_dec_values):
    decrypted_value = val ^ ord(xor_key[pos])
    decrypted_values.append(decrypted_value)

print(decrypted_values)
print()

print("Plaintext String:")
for i in decrypted_values:
    print(chr(i), end="")