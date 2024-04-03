class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""


def calcul_probabilite(msg: str) -> dict:
    probability = {}
    for symbol in msg:
        if symbol not in probability:
            probability[symbol] = 1
        else:
            probability[symbol] += 1
    return probability


codes = {}


def calculate_codes(node: Node, val="") -> dict:
    """Calculate encoding code for each symbol"""
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)

    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes


def create_huffman_tree(nodes: list) -> list:
    """create huffman tree to the root from list of leaf nodes"""
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]

        right.code = 1
        left.code = 0

        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    return nodes[0]


def output_encoded(data: str, symbol_with_code: dict) -> str:
    """Print full encoded string"""
    strList = []
    for character in data:
        strList.append(symbol_with_code[character])

    joinedStr = "".join(strList)
    return joinedStr


def huffman_encoding(msg: str):
    symbol_with_prob = calcul_probabilite(msg)
    nodes = []
    for symbol in symbol_with_prob:
        nodes.append(Node(symbol_with_prob[symbol], symbol))

    list_of_nodes = [(node.symbol, node.prob) for node in nodes]

    huffman_tree = create_huffman_tree(nodes)

    # Menggunakan nodes[0] karena hanya tersisa satu node (yaitu root) dalam nodes list
    symbol_with_code = calculate_codes(huffman_tree)
    output_encoded_str = output_encoded(msg, symbol_with_code)

    return (
        output_encoded_str,
        huffman_tree,
    )


def huffman_decoding(encoded_data: str, huffman_tree: Node):
    tree_head = huffman_tree
    decoded_output = []

    for x in encoded_data:
        if x == "1":
            huffman_tree = huffman_tree.right
        elif x == "0":
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = "".join([str(item) for item in decoded_output])
    return string
