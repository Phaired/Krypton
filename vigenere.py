def vigenere_encode(msg: str, key: str) -> str:
    """
    Encode un message avec le chiffrement de Vigenère
    :param msg: Message à encoder
    :param key: Clé de chiffrement
    :return: Message encodé avec le chiffrement de Vigenère
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    keyIndex = 0
    for i in range(len(msg)):
        column = alphabet.find(msg[i].lower())
        row = alphabet.find(key[keyIndex].lower())
        if column == -1:
            result += msg[i]
        else:
            if (msg[i].isupper()):
                result += alphabet[(row + column) % 26].upper()
            else:
                result += alphabet[(row + column) % 26]
            keyIndex = (keyIndex + 1) % len(key)
    return result


def vigenere_decode(msg: str, key: str) -> str:
    """
    Décode un message avec le chiffrement de Vigenère
    :param msg: Message à décoder
    :param key: Clé de chiffrement
    :return: Message décodé avec le chiffrement de Vigenère
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    keyIndex = 0
    for i in range(len(msg)):
        column = alphabet.find(msg[i].lower())
        row = alphabet.find(key[keyIndex].lower())
        if column == -1:
            result += msg[i]
        else:
            if (msg[i].isupper()):
                result += alphabet[(column - row) % 26].upper()
            else:
                result += alphabet[(column - row) % 26]
            keyIndex = (keyIndex + 1) % len(key)
    return result
