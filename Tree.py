from Node import Node

class Tree(Node):
    def __init__(self):
        self.root = Node(None)
        self.numFilhos = 0

    def generateTree(self, nodo, nivel):
        newNode = Node(nivel);
        if nivel == 0:
            return
        for i in range(nivel):
            nodo.= newNode
            self.generateTree(nodo.filhos[i], nivel-1)
            self.numFilhos = self.numFilhos + 1