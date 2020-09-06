import base64


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
numbers = "1234567890"


def encryptCaesar(msg, shift):
    result = ""
    for i in range(len(msg)):
        letter = msg[i]

        if letter not in alphabet:
            result += letter
            continue
        elif letter in numbers:
            result += str((int(letter) + (shift % 10)) % 10)
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
        elif letter in numbers:
            result += str((int(letter) - (shift % 10)) % 10)
        elif letter.isupper():
            result += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(letter) - shift - 97) % 26 + 97)
    return result


def decryptCaesarBrute(msg):
    for key in range(26):
        print("Shift by #" + str(key) + " \"" + decryptCaesar(msg, key) + "\"")


def encryptBase64(msg):
    result = base64.b16encode(msg.encode('utf-8')).decode('utf-8')
    return result


def decryptBase64(msg):
    result = base64.b16decode(msg.encode('utf-8')).decode('utf-8')
    return result


print("Welcome to Spypher!")
while True:
    print("Please select an option:")
    print("\tE: Encrypt")
    print("\tD: Decrypt")
    print("\tQ: Quit")

    userInput = str(input())

    if userInput.upper() == "Q":
        print("Exiting...")
        exit()

    if userInput.upper() == "E":
        message = str(input("Please enter message to encrypt:\n"))
        print("Please select a method to use:")
        print("\tC: Caesar Cipher")
        print("\tB: Base64 Encryption")
        print("\tQ: Quit")

        userInput = str(input())

        if userInput.upper() == "Q":
            print("Exiting...")
            exit()

        if userInput.upper() == "C":
            shiftNum = int(input("Please enter number to shift by(1-25):\n"))
            while shiftNum > 25 or shiftNum < 1:
                print("ERROR: Invalid number!")
                shiftNum = int(input("Please enter a number to shift by(1-25):\n"))
            print(encryptCaesar(message, shiftNum))

        if userInput.upper() == "B":
            print(encryptBase64(message))

    if userInput.upper() == "D":
        message = str(input("Please enter message to decrypt:\n"))
        print("Please select a method to use:")
        print("\tC: Caesar Cipher")
        print("\tCB: Casear Cipher Brute Force")
        print("\tB: Base64 Encryption")
        print("\tQ: Quit")

        userInput = str(input())

        if userInput.upper() == "Q":
            print("Exiting...")
            exit()

        if userInput.upper() == "C":
            shiftNum = int(input("Please enter the number the message is shifted by:\n"))
            print(decryptCaesar(message, shiftNum))

        if userInput.upper() == "CB":
            decryptCaesarBrute(message)

        if userInput.upper() == "B":
            print(decryptBase64(message))


