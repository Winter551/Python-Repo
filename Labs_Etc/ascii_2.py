MyPlainText = "ABCDE"
XOR_KEY =     "PASSW"

Encrypted_Values = []


for Position, PlainTextCharacter in enumerate(MyPlainText):
    print(Position, PlainTextCharacter)
    print(Position, XOR_KEY[Position])
    encrypted_byte = ord(PlainTextCharacter) ^ ord(XOR_KEY[Position])

    Encrypted_Values.append(encrypted_byte)


print(Encrypted_Values)

print("Hex Values: ")
for i in Encrypted_Values:
    print(hex(i) + " ", end="")

print()

print("Hex Values without 0x: ")

for i in Encrypted_Values:
    print(format(i,"x") + " ", end="")