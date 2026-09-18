def Encription():
    shift_number = int(input("Enter your shift number: "))
    text = input("Enter your text: ")


    def shift_character(char):
        if char.islower():
            return chr((ord(char) - ord('a') + shift_number) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') + shift_number) % 26 + ord('A'))
        else:
            return char

    encrypted_text = ""
    for char in text:
        encrypted_text += shift_character(char)

    return encrypted_text


def Decryption():
    shift_number = int(input("Enter your shift number: "))
    text = input("Enter your text: ")


    def shift_character(char):
        if char.islower():
            return chr((ord(char) - ord('a') - shift_number) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') - shift_number) % 26 + ord('A'))
        else:
            return char


    encrypted_text = ""
    for char in text:
        encrypted_text += shift_character(char)

    return encrypted_text

print('Encrypting')
print("Encrypted: ",Encription())
print('-------------------------------------')
print('Decrypting')
print("Decrypted: ",Decryption())
