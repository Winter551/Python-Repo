originaltext = "PlainText"
key = "ABC"

print(originaltext)

for pos, letter in enumerate(originaltext):
    x = key[pos % len(key)]
    print(x,end="")

print()

encrypted_values = []

for pos, letter in enumerate(originaltext):
    letter_key = key[pos % len(key)]
    encrypted_byte = ord(letter) ^ ord(letter_key)
    encrypted_values.append(encrypted_byte)

print(encrypted_values)

for i in encrypted_values:
    print(hex(i) + " ", end="")
print()

for i in encrypted_values:
    print(format(i,"x") + " ", end="")