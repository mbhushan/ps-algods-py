from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    dataSet = set([])
    values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    for r in range(random.randint(7, 12)):
        n = random.randint(1, 100)
        dataSet.add(n)

    print ("Inserting into Binary Tree: ")
    for data in dataSet:
    # for data in values:
        bt.insert(data)
        print (data, sep=" ", end=" ")
    print ()

    print ("Inorder: ")
    bt.inorder()
    print ("Preorder: ")
    bt.preorder()
    print ("postorder: ")
    bt.postorder()
    print ("Binary Tree Size: ", bt.size())
    print ("Max Depth: ", bt.maxdepth())
    print ("Min value in BST: ", bt.minvalue())
    print ("Max value in BST: ", bt.maxvalue())


if __name__ == '__main__':
    main()
