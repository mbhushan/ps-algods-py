
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

    def size(self):
        return self.N
