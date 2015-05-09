import gens, BinSearchTree

tutti = [] # to hold a list of all people
for i in range(0,1000): # making 1000 people
    tutti.append( gens.Gens('Fred_' + str(i)) )
    
bst = BinSearchTree.BinSearchTree()
print('The tree has ' + str(bst.getSize()) + ' people in it')
for i in range(0,10):
    bst.insert(tutti[9 - i])
    print('\tAdding ' + tutti[9-i].info())
print('The tree has ' + str(bst.getSize()) + ' people in it')
bst.printLR()

