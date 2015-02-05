
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

    def minvalue(self):
        def minvalbst(node):
            if node is None:
                return None
            while node.left is not None:
                node = node.left
            return node.data
        return minvalbst(self.root)

    def maxvalue(self):
        def maxvalbst(node):
            if node is None:
                return None
            while node.right is not None:
                node = node.right
            return node.data
        return maxvalbst(self.root)

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

    def preorder(self):
        def preorderBT(node):
            if node is None:
                return
            print (node.data, sep=" ", end=" ")
            preorderBT(node.left)
            preorderBT(node.right)
        preorderBT(self.root)
        print ()

    def postorder(self):
        def postorderBT(node):
            if node is None:
                return
            postorderBT(node.left)
            postorderBT(node.right)
            print (node.data, sep=" ", end=" ")
        postorderBT(self.root)
        print ()

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
