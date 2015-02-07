from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    dataSet = set([])
    # values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    values = [25, 15, 40, 10, 20, 30, 50, 18, 22, 27, 45, 60, 42, 47, 49]
    for r in range(random.randint(7, 12)):
        n = random.randint(1, 100)
        dataSet.add(n)

    print ("Inserting into Binary Tree: ")
    # for data in dataSet:
    for data in values:
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

    targetsums = [50, 78, 82, 97, 150]
    for target in targetsums:
        ans = bt.haspathsum(target)
        print ("Sum: %d in binary tree: %s" % (target, ans))

    print ("print all the root to leaf paths in binary tree")
    bt.printpaths()
    print ("Mirroring the binary tree: ")
    bt.mirror()
    bt.inorder()

    bt = BinaryTree()
    values = [2, 3, 1]
    print ("Inserting into Binary Tree: ")
    # for data in dataSet:
    for data in values:
        bt.insert(data)
        print (data, sep=" ", end=" ")
    print ()
    bt.inorder()
    print ("After doing double tree: ")
    bt.doubletree()
    bt.inorder()




if __name__ == '__main__':
    main()
