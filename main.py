

def applyCipher(plaintext):
    key = ''
    while 1:
        key = input("Please enter the key you would like to use for the Vigenere Cipher: ")
        response = input("Is '" + key + "' the key you want to use? [y/n] ")
        key = key.lower()
        if response == "y" or response == "yes":
            break
    plaintext = plaintext.lower()
    plaintextList = convertToNum(plaintext)
    print("The plaintext converted to numbers, where a = 0 and z = 25 is:", plaintextList)
    keyList = convertToNum(key)
    print("The key converted to numbers, where a = 0 and z = 25 is: ", keyList)
    keyLength = len(keyList)
    for i in range(0,len(plaintextList)):
        plaintextList[i] = (plaintextList[i] + keyList[i % keyLength]) % 26
    print("After running the Vigenere Cipher, the new numerical representation is:", plaintextList)
    cipherText = convertToString(plaintextList)
    print("This leaves us with the final Cipher Text of:", cipherText)
    return cipherText

def findKey(plaintext):
    ciphertext = ''
    while 1:
        ciphertext = input("Please enter the ciphertext you would like to use for the Vigenere Cipher: ")
        response = input("Is '" + ciphertext + "' the key you want to use? [y/n] ")
        ciphertext = ciphertext.lower().replace(" ", "")
        if response == "y" or response == "yes":
            break
    plaintext = plaintext.lower()
    plaintextList = convertToNum(plaintext)
    print("The plaintext converted to numbers, where a = 0 and z = 25 is:", plaintextList)
    cipherList = convertToNum(ciphertext)
    print("The ciphertext converted to numbers, where a = 0 and z = 25 is: ", cipherList)
    pattern = []
    for i in range(0,len(cipherList)):
        pattern.append((cipherList[i] - plaintextList[i]) % 26)
    print("If we subtract the plaintext from the ciphertext, we are left with the following pattern:", pattern)
    return pattern



def convertToNum(string):
    result = []
    for i in string:
        result.append(ord(i) - 97)
    return result

def convertToString(lst):
    result = ''
    for i in lst:
        result+= chr(i+97)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        plaintext = input("Please enter the plaintext you would like to use for the Vigenere Cipher: ")
        response = input("Is '" + plaintext + "' the plaintext you want to use? [y/n] ")
        if response == "y" or response == "yes":
            apply = input("Would you like to apply a Vigenere Cipher on plaintext? [y/n] ")
            if apply == "y" or apply == "yes":
                applyCipher(plaintext.replace(" ",""))
                break
            deduce = input("Would you like to decode a Vigenere Cipher using plaintext and ciphertext? [y/n] ")
            if deduce == "y" or deduce == "yes":
                findKey(plaintext.replace(" ", ""))
                break
