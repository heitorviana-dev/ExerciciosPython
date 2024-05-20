class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if data < current_node.data:  # Verifica se é menor para entrar na esquerda
                    if not current_node.left:  # Verifica se existe um nó à esquerda
                        current_node.left = Node(data)
                        break
                    else:  # Atribui ao nó atual o nó da esquerda para continuar até achar um vazio
                        current_node = current_node.left
                elif data > current_node.data:  # Verifica se é maior para entrar à direita
                    if not current_node.right:  # Verifica se existe um nó à direita
                        current_node.right = Node(data)
                        break
                    else:  # Atribui ao nó atual o nó da direita para continuar até achar um vazio
                        current_node = current_node.right
                else:
                    print("O valor já existe na árvore.")
                    break



