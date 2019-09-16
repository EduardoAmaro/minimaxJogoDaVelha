class Node(object):
    def __init__(self, board, height):
        self.height = height
        self.children = []
        self.board = board
        for i in range(0, height):
            self.children.append(None)
