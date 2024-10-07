PRODIGY_CS_01
#  Caesar Cipher Encryption and Decryption

This project implements the Caesar Cipher algorithm in Python. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a specific number of positions, defined by a "key," in the alphabet. Both encryption and decryption are supported using mod 26 to ensure proper letter wrapping. The program also includes input validation to ensure the key is an integer.


## Features

- Encrypts and decrypts messages using the Caesar Cipher algorithm.

- Supports both uppercase and lowercase letters.

- Non-alphabetic characters (e.g., spaces, punctuation) remain unchanged.

- User can input any shift value (key) for the cipher with validation to ensure it is an integer.


## How It Works

### Encryption:

-Each letter in the plain text is shifted by a certain number of positions (key) in the alphabet:

-Uppercase letters (A-Z) are shifted within the range of 'A' to 'Z'.

-Lowercase letters (a-z) are shifted within the range of 'a' to 'z'.

-Non-alphabetic characters are not modified.


### Decryption:

The decryption process reverses the encryption by shifting the letters back by the same key value.
