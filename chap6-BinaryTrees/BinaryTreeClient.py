from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    dataSet = set([])
    # values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    values = [25, 15, 40, 10, 20, 30, 50, 18, 22, 27, 45, 60]
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


if __name__ == '__main__':
    main()
