from hamming import *
from vigenere import *

if __name__ == "__main__":
    with open("message.txt", "r") as file:
        binMessage = file.read()
        key = "PYTHON"
        binMessage = hamming_decode(binMessage)
        print(f"Message décodé : {binMessage}")

        asciiMessage = ""
        for i in range(0, len(binMessage), 8):
            buffer = binMessage[i:i + 8]
            asciiMessage += chr(int(buffer, 2))

        print(f"Message ASCII : {asciiMessage}")
        print(f"Message ASCII décodé : {vigenere_decode(asciiMessage, key)}")