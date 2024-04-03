from random import random


def vernam_encode(msg: str) -> (str, str):
    """
    Encode un message avec le chiffrement de Vernam
    :param msg: Message à encoder
    :return: Message encodé avec le chiffrement de Vernam et la clé utilisée
    """

    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(msg)):
        key += alphabet[int(random() * 26)]

    result = ""
    for i in range(len(msg)):
        indexCharMsg = alphabet.find(msg[i].lower())
        indexCharKey = alphabet.find(key[i].lower())

        if indexCharMsg != -1 and indexCharKey != -1:
            if msg[i].isupper():
                result += alphabet[(indexCharMsg + indexCharKey) % 26].upper()
            else:
                result += alphabet[(indexCharMsg + indexCharKey) % 26]
        else:
            # char non trouvé dans l'alphabet donc on le laisse tel quel
            result += msg[i]

    return result, key


def vernam_decode(msg: str, key: str) -> str:
    """
    Décode un message avec le chiffrement de Vernam
    :param msg: Message à décoder
    :param key: Clé de chiffrement
    :return: Message décodé avec le chiffrement de Vernam
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(msg)):
        indexCharMsg = alphabet.find(msg[i].lower())
        indexCharKey = alphabet.find(key[i].lower())

        if indexCharMsg != -1 and indexCharKey != -1:
            if msg[i].isupper():
                result += alphabet[(indexCharMsg - indexCharKey) % 26].upper()
            else:
                result += alphabet[(indexCharMsg - indexCharKey) % 26]
        else:
            # char non trouvé dans l'alphabet donc on le laisse tel quel
            result += msg[i]

    return result
