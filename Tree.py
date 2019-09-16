import Node


class Tree(object):
    def __init__(self, board, height):
        self.root = Node.Node(board, height)

    def generate_tree(self, node, height):
        if height == 0:  # last node
            return None
        else:
            for i in range(0, height):
                board = self.copy_board(node.board)  # copy root board to a new board

                if (height % 2) == 0:  # verify player
                    next_player = 'O'
                else:
                    next_player = 'X'

                self.move(board, next_player, i)  # makes a move to the copied board
                win = self.verify_win(board)  # verify win
                if win == 0:  # not win
                    node.children[i] = Node.Node(board, height - 1)
                    self.generate_tree(node.children[i], height - 1)
                else:  # win
                    node.children[i] = Node.Node(board, 0)

    def counter(self, node, height, cont=0):
        if height == 0:
            return 1
        else:
            elements = node.children
            for child in elements:
                cont += self.counter(child, height - 1)
        return cont

    def verify_win(self, board):
        # check row
        for i in range(0, 3):
            if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][0] != '-'):
                if board[i][0] == 'X':
                    return 1
                else:
                    return -1
        # check col
        for j in range(0, 3):
            if (board[0][j] == board[1][j]) and (board[1][j] == board[2][j]) and (board[0][j] != '-'):
                if board[0][j] == 'X':
                    return 1
                else:
                    return -1
        # check diagonal
        if (((board[0][0] == board[1][1]) and (board[1][1] == board[2][2])) or ((board[0][2] == board[1][1])
                                                                                and (board[1][1] == board[2][0]))) and (
                board[1][1] != '-'):
            if board[0][0] == 'X':
                return 1
            else:
                return -1
        return 0

    def copy_board(self, board):
        new_board = [['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']]
        for i in range(0, 3):
            for j in range(0, 3):
                new_board[i][j] = board[i][j]
        return new_board

    def move(self, board, player, i):
        x = 0
        y = 0
        z = 0
        while x != i:
            if board[y][z] == '-':
                x += 1
            z += 1
            if z == 3:
                y += 1
                z = 0
        while y < 3:
            if board[y][z] == '-':
                board[y][z] = player
                break
            z += 1
            if z == 3:
                y += 1
                z = 0

    def show_board(self, board):
        for i in range(0, 3):
            for j in range(0, 3):
                print('[' + board[i][j] + ']', end='')
            print('\n')

    def minimax(self, node, height, flag_max):
        if node.height == 1:
            return self.verify_win(node.board)
        elif not flag_max:
            alpha = 10000
            children = node.children
            for child in children:
                alpha = min(alpha, self.minimax(child, height - 1, True))
            return alpha
        else:
            alpha = -10000
            children = node.children
            for child in children:
                alpha = max(alpha, self.minimax(child, height - 1, False))
            return alpha
