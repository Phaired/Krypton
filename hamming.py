def hamming_decode(msg: str) -> str:  # TODO : Utiliser un type bytes/binary au lieu de string
    """
    Décode un message encodé avec le code de Hamming, corrige les erreurs et retire les bits de redondance
    :param msg: Message encodé avec le code de Hamming
    :return: Message décodé, corrige et sans bits de redondance
    """
    result = ""
    for i in range(0, len(msg), 7):
        buffer = msg[i:i + 4]
        redondance = [
            int(msg[i + 4]),
            int(msg[i + 5]),
            int(msg[i + 6])
        ]
        computedRedondance = [
            int(buffer[0]) ^ int(buffer[1]) ^ int(buffer[2]),
            int(buffer[0]) ^ int(buffer[1]) ^ int(buffer[3]),
            int(buffer[1]) ^ int(buffer[2]) ^ int(buffer[3])
        ]

        if redondance != computedRedondance:
            # Calcul de la position de l'erreur
            redondanceDistance = [
                redondance[0] == computedRedondance[0],
                redondance[1] == computedRedondance[1],
                redondance[2] == computedRedondance[2]
            ]

            errorIndex = 0
            match redondanceDistance:
                case [False, False, True]:
                    errorIndex = 0
                case [False, False, False]:
                    errorIndex = 1
                case [False, True, False]:
                    errorIndex = 2
                case [True, False, False]:
                    errorIndex = 3

            # Correction de l'erreur
            buffer = list(buffer)
            buffer[errorIndex] = str(int(buffer[errorIndex]) ^ 1)
            buffer = "".join(buffer)

        result += buffer

    return result


def hamming_encode(msg: str) -> str:  # TODO : Utiliser un type bytes/binary au lieu de string
    """
    Encode un message avec le code de Hamming
    :param msg: Message à encoder
    :return: Message encodé avec le code de Hamming
    """
    result = ""
    for i in range(0, len(msg), 4):
        buffer = msg[i:i + 4]
        result += buffer
        result += str(int(buffer[0]) ^ int(buffer[1]) ^ int(buffer[2]))
        result += str(int(buffer[0]) ^ int(buffer[1]) ^ int(buffer[3]))
        result += str(int(buffer[1]) ^ int(buffer[2]) ^ int(buffer[3]))

    return result
