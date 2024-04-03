from hamming import *
from vigenere import *
from vernam import *

if __name__ == "__main__":
    with open("message.txt", "r") as file:
        binMessage = file.read()
        print(f"Message initial : {binMessage}")
        key = "PYTHON"
        binMessage = hamming_decode(binMessage)
        print(f"Message décodé : {binMessage}")

        asciiMessage = ""
        for i in range(0, len(binMessage), 8):
            buffer = binMessage[i:i + 8]
            asciiMessage += chr(int(buffer, 2))

        print(f"Message ASCII : {asciiMessage}")
        asciiMessageDecode = vigenere_decode(asciiMessage, key)
        print(f"Message ASCII décodé : {asciiMessageDecode}")

        vernamMessage, vernamKey = vernam_encode(asciiMessageDecode)
        print(f"Message ASCII vernam : {vernamMessage}")
        print(f"Clé vernam : {vernamKey}")
        print(f"Message ASCII vernam décodé : {vernam_decode(vernamMessage, vernamKey)}")