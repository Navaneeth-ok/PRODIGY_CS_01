# Caesar Cipher 
def encryption(plain, key):
    string = ""
    for char in plain:
        if char.isupper():  # Encrypt uppercase letters
            new_character = chr((ord(char) - 65 + key) % 26 + 65)
            string += new_character
        elif char.islower():  # Encrypt lowercase letters
            new_character = chr((ord(char) - 97 + key) % 26 + 97)
            string += new_character
        else:
            string += char  # Non-alphabetic characters remain unchanged
    return string


def decryption(cipher_text, key):
    string = ""
    for char in cipher_text:
        if char.isupper():  # Decrypt uppercase letters
            new_character = chr((ord(char) - 65 - key) % 26 + 65)
            string += new_character
        elif char.islower():  # Decrypt lowercase letters
            new_character = chr((ord(char) - 97 - key) % 26 + 97)
            string += new_character
        else:
            string += char  # Non-alphabetic characters remain unchanged
    return string


plain = input("Enter the plain text: ")


while True:
    try:
        key = int(input("Enter the key (shift value): "))
        break  
    except ValueError:
        print("Key can't be an alphabet. Please enter an integer value.")

# Encryption
cipher_text = encryption(plain, key)
print("Encrypted text:", cipher_text)

# Decryption
plain_text = decryption(cipher_text, key)
print("Decrypted text:", plain_text)
