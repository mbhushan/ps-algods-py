from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    dataSet = set([])
    for r in range(random.randint(7, 12)):
        n = random.randint(1, 100)
        dataSet.add(n)

    print ("Inserting into Binary Tree: ")
    for data in dataSet:
        bt.insert(data)
        print (data, sep=" ", end=" ")
    print ()

    print ("Inorder: ")
    bt.inorder()
    print ("Binary Tree Size: ", bt.size())
    print ("Max Depth: ", bt.maxdepth())


if __name__ == '__main__':
    main()
