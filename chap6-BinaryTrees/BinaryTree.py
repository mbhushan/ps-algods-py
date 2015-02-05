
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.N = 0

    def insert(self, data):
        def insertBST(node, data):
            if node is None:
                return Node(data)
            if data <= node.data:
                node.left = insertBST(node.left, data)
            else:
                node.right = insertBST(node.right, data)
            return node

        self.root = insertBST(self.root, data)

    def maxdepth(self):
        def maxdepthBT(node):
            if node is None:
                return 0
            left = maxdepthBT(node.left)
            right = maxdepthBT(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1
        return maxdepthBT(self.root)

    def size(self):
        def sizebt(node):
            if node is None:
                return 0
            return (sizebt(node.left) + 1 + sizebt(node.right))
        return sizebt(self.root)

    def inorder(self):
        def inorderBST(node):
            if node is None:
                return
            inorderBST(node.left)
            print (node.data, sep=" ", end=" ")
            inorderBST(node.right)

        inorderBST(self.root)
        print ()

    def isempty(self):
        return self.N == 0
