class Node:
    def __init__(self, occ, character, left=None, right=None):
        self.occ = occ
        self.character = character
        self.left = left
        self.right = right
        self.code = ""


def calcul_occurence(msg: str) -> dict:
    """
    Calculer le nombre d'occurence de chaque caractère dans un message
    :param msg: le message à analyser
    :return: un dictionnaire avec le nombre d'occurence de chaque caractère
    """
    occurence = {}
    for character in msg:
        if character not in occurence:
            occurence[character] = 1
        else:
            occurence[character] += 1
    return occurence


# Dictionnaire pour stocker les codes de chaque caractère
codes = {}


def calculate_codes(node: Node, val="") -> dict:
    """
    Calculer les codes de chaque caractère dans un arbre de Huffman
    :param node: Le noeud tête de l'arbre de Huffman
    :param val: La valeur actuelle du noeud (par défaut "", permet de récursivement calculer les codes de chaque caractère
    :return: Un dictionnaire avec les codes de chaque caractère
    """
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)

    if not node.left and not node.right:
        codes[node.character] = newVal

    return codes


def create_huffman_tree(nodes: list) -> list:
    """
    Créer un arbre de Huffman à partir d'une liste de noeuds ordonnée par occurence croissante
    :param nodes: Liste des noeuds
    :return: Le noeud tête de l'arbre de Huffman
    """
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.occ)
        right = nodes[0]
        left = nodes[1]

        right.code = 1
        left.code = 0

        newNode = Node(left.occ + right.occ, left.character + right.character, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    return nodes[0]


def output_encoded(data: str, symbol_with_code: dict) -> str:
    """
    Converti le message initial en un message encodé avec les codes de Huffman
    :param data: le message initial
    :param symbol_with_code: le dictionnaire des codes de chaque caractère
    :return:
    """
    strList = []
    for character in data:
        strList.append(symbol_with_code[character])

    joinedStr = "".join(strList)
    return joinedStr


def huffman_encoding(msg: str) -> (str, Node):
    """
    Encode un message avec le codage de Huffman
    :param msg: Le message à encoder
    :return: Le message encodé et l'arbre de Huffman
    """
    char_occ = calcul_occurence(msg)
    nodes = []
    for character in char_occ:
        nodes.append(Node(char_occ[character], character))

    huffman_tree = create_huffman_tree(nodes)

    symbol_with_code = calculate_codes(huffman_tree)
    output_encoded_str = output_encoded(msg, symbol_with_code)

    return (
        output_encoded_str,
        huffman_tree,
    )


def huffman_decoding(encoded_data: str, huffman_tree: Node) -> str:
    """
    Décode un message encodé avec le codage de Huffman
    :param encoded_data: Le message encodé
    :param huffman_tree: L'arbre de Huffman
    :return: Le message décodé
    """
    tree_head = huffman_tree
    decoded_output = []

    for x in encoded_data:
        if x == "1":
            huffman_tree = huffman_tree.right
        elif x == "0":
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.character == None and huffman_tree.right.character == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.character)
            huffman_tree = tree_head

    results = "".join([str(item) for item in decoded_output])
    return results
