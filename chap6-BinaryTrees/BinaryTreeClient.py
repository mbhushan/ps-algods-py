from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    for r in range(10):
        n = random.randint(1, 100)
        bt.insert(n)
    bt.inorder()


if __name__ == '__main__':
    main()
