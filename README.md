# VigenereCipher
### Made By Jonathan Leibovich

This is a very simple python script that helped me encode and decode Vigenere Ciphers for MATH 5248 (Cryptology and Number Theory) at the University of Minnesota

## How to Run
Simply run the main script using Python v3+
``` bash.sh
python3 ./main.py
```

## Usage
### Encoding using a Vigenere Cipher
After running the program, simply follow the prompts as they are given. After deciding what operation you would like 
to do, the rest should be pretty straight forward.

Example Encode:
```
> Would you like to Encode, Decode, or find the Key of a Vigenere Cipher? [encode, decode, key] encode
> Please enter the plaintext you would like to use for the Vigenere Cipher: hello world
> Is 'hello world' the plaintext you want to use? [y/n] y
> Please enter the key you would like to use for the Vigenere Cipher: abcd
> Is 'abcd' the key you want to use? [y/n] y
> The plaintext converted to numbers, where a = 0 and z = 25 is: [7, 4, 11, 11, 14, 22, 14, 17, 11, 3]
> The key converted to numbers, where a = 0 and z = 25 is:  [0, 1, 2, 3]
> After running the Vigenere Cipher, the new numerical representation is: [7, 5, 13, 14, 14, 23, 16, 20, 11, 4]
> This leaves us with the final Cipher Text of: hfnooxqule
```

Example Decode:
```
> Would you like to Encode, Decode, or find the Key of a Vigenere Cipher? [encode, decode, key] decode
> Please enter the ciphertext you would like to use for the Vigenere Cipher: hfnooxqule
> Is 'hfnooxqule' the ciphertext you want to use? [y/n] y
> Please enter the key you would like to use for the Vigenere Cipher: abcd
> Is 'abcd' the key you want to use? [y/n] y
> The plaintext converted to numbers, where a = 0 and z = 25 is: [7, 5, 13, 14, 14, 23, 16, 20, 11, 4]
> The key converted to numbers, where a = 0 and z = 25 is:  [0, 1, 2, 3]
> After running the Vigenere Cipher, the new numerical representation is: [7, 4, 11, 11, 14, 22, 14, 17, 11, 3]
> This leaves us with the final Cipher Text of: helloworld
```

Example Key find:
```
> Would you like to Encode, Decode, or find the Key of a Vigenere Cipher? [encode, decode, key] key
> Please enter the plaintext you would like to use for the Vigenere Cipher: hello world
> Is 'hello world' the plaintext you want to use? [y/n] y
> Please enter the ciphertext you would like to use for the Vigenere Cipher: hfnooxqule
> Is 'hfnooxqule' the key you want to use? [y/n] y
> The plaintext converted to numbers, where a = 0 and z = 25 is: [7, 4, 11, 11, 14, 22, 14, 17, 11, 3]
> The ciphertext converted to numbers, where a = 0 and z = 25 is:  [7, 5, 13, 14, 14, 23, 16, 20, 11, 4]
> If we subtract the plaintext from the ciphertext, we are left with the following pattern: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
```