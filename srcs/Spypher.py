alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryptCaesar(msg, shift):
    result = ""
    for i in range(len(msg)):
        letter = msg[i]

        if letter not in alphabet:
            result += letter
            continue
        elif letter.isupper():
            result += chr((ord(letter) + shift-65) % 26 + 65)
        else:
            result += chr((ord(letter) + shift - 97) % 26 + 97)
    return result


def decryptCaesar(msg, shift):
    result = ""
    for i in range(len(msg)):
        letter = msg[i]

        if letter not in alphabet:
            result += letter
            continue
        elif letter.isupper():
            result += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(letter) - shift - 97) % 26 + 97)
    return result


print("Welcome to Spypher!")
print("Please select an option:")
print("\tE: Encrypt")
print("\tD: Decrypt")

userInput = str(input())

if userInput.upper() == "E":
    message = str(input("Please enter message to encrypt:\n"))
    print("Please select a method to use:")
    print("\tC: Caesar Cipher")
    print("\tB: Base64 Encryption")

    userInput = str(input())

    if userInput.upper() == "C":
        shiftNum = int(input("Please enter number to shift by:\n"))
        print(encryptCaesar(message, shiftNum))

if userInput.upper() == "D":
    message = str(input("Please enter message to decrypt:\n"))
    print("Please select a method to use:")
    print("\tC: Caesar Cipher")

    userInput = str(input())

    if userInput.upper() == "C":
        shiftNum = int(input("Please enter the number the message is shifted by:\n"))
        print(decryptCaesar(message, shiftNum))
