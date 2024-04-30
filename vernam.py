from random import random

alphabet = "abcdefghijklmnopqrstuvwxyz, 0123456789"

def vernam_encode(msg: str) -> (str, str):
    """
    Encode un message avec le chiffrement de Vernam
    :param msg: Message à encoder
    :return: Message encodé avec le chiffrement de Vernam et la clé utilisée
    """

    key = ""
    for i in range(len(msg)):
        key += alphabet[int(random() * len(alphabet))]

    result = ""
    for i in range(len(msg)):
        indexCharMsg = alphabet.find(msg[i].lower())
        indexCharKey = alphabet.find(key[i].lower())

        if indexCharMsg != -1 and indexCharKey != -1:
            if msg[i].isupper():
                result += alphabet[(indexCharMsg + indexCharKey) % len(alphabet)].upper()
            else:
                result += alphabet[(indexCharMsg + indexCharKey) % len(alphabet)]
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
    result = ""
    for i in range(len(msg)):
        indexCharMsg = alphabet.find(msg[i].lower())
        indexCharKey = alphabet.find(key[i].lower())

        if indexCharMsg != -1 and indexCharKey != -1:
            if msg[i].isupper():
                result += alphabet[(indexCharMsg - indexCharKey) % len(alphabet)].upper()
            else:
                result += alphabet[(indexCharMsg - indexCharKey) % len(alphabet)]
        else:
            # char non trouvé dans l'alphabet donc on le laisse tel quel
            result += msg[i]

    return result
