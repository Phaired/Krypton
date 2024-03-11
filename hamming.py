def hamming_decode(msg: str) -> str:
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

            print(f"Erreur détectée à l'indice {i}")
            print(f"Redondance attendue : {redondance}, redondance calculée : {computedRedondance}")
            print(f"Verification de la redondance : {redondanceDistance}")
            print(f"Indice de l'erreur : {errorIndex}")

            # Correction de l'erreur
            print(f"Message erroné : {buffer}")
            buffer = list(buffer)
            buffer[errorIndex] = str(int(buffer[errorIndex]) ^ 1)
            buffer = "".join(buffer)
            print(f"Message corrigé : {buffer}")

        result += buffer

    return result


if __name__ == "__main__":
    with open("message.txt", "r") as file:
        msg = file.read()
        print(hamming_decode(msg))