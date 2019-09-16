import Tree

initial_board = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]

arvore = Tree.Tree(initial_board, 9)
arvore.generate_tree(arvore.root, 9)
print(arvore.counter(arvore.root, 9, 0))
print(arvore.minimax(arvore.root, 9, True))
#arvore.show_board(arvore.root.children[1].children[2].children[2].children[2].board)
#arvore.show_board(arvore.root.children[0].children[2].board)
'''
for i in range(0, 9):
    arvore.show_board(arvore.root.children[i].board)
    #arvore.show_board(arvore.root.children[i].children[0].board)
    for j in range(0, 8):
        arvore.show_board(arvore.root.children[i].children[j].board)
        for k in range(0, 7):
            arvore.show_board(arvore.root.children[i].children[j].children[k].board)
            for l in range(0, 6):
                arvore.show_board(arvore.root.children[i].children[j].children[k].children[l].board)
                for m in range(0, 5):
                    arvore.show_board(arvore.root.children[i].children[j].children[k].children[l].children[m].board)
'''
