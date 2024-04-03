from hamming import *
from vigenere import *
from vernam import *

if __name__ == "__main__":
    with open("message.txt", "r") as file:
        binMessage = file.read()
        print(f"Message initial : {binMessage}")

        with open("Etape1 - message initial.txt", "w") as file:
            file.write(binMessage)

        key = "PYTHON"
        binMessage = hamming_decode(binMessage)
        print(f"Message décodé : {binMessage}")

        with open("Etape2 - message decode et corrige.txt", "w") as file:
            file.write(binMessage)

        asciiMessage = ""
        for i in range(0, len(binMessage), 8):
            buffer = binMessage[i:i + 8]
            asciiMessage += chr(int(buffer, 2))

        with open("Etape3 - message ASCII.txt", "w") as file:
            file.write(asciiMessage)

        print(f"Message ASCII : {asciiMessage}")
        asciiMessageDecode = vigenere_decode(asciiMessage, key)

        with open("Etape4 - message ASCII decode.txt", "w") as file:
            file.write(asciiMessageDecode)

        print(f"Message ASCII décodé : {asciiMessageDecode}")
        vernamMessage, vernamKey = vernam_encode(asciiMessageDecode)

        with open("Etape5 - message ASCII vernam.txt", "w") as file:
            file.write(vernamMessage)

        with open("Etape5 - cle vernam.txt", "w") as file:
            file.write(vernamKey)

        print(f"Message ASCII vernam : {vernamMessage}")
        print(f"Clé vernam : {vernamKey}")
        vernamMessage = vernam_decode(vernamMessage, vernamKey)

        with open("Etape6 - message ASCII vernam decode.txt", "w") as file:
            file.write(vernamMessage)

        print(f"Message ASCII vernam décodé : {vernamMessage}")
