class Node:
    def __init__(self, profundidade):
        self.profundidade = profundidade
        self.filhos = []
        self.tabuleiro = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
