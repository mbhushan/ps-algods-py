import sys


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.N = 0

    def getrootnode(self):
        return self.root

    def isbst2(self):
        """ Returns true if the given tree is a binary search tree
        (efficient version). """
        def isbst_util(node, mini, maxi):
            if node is None:
                return True
            if node.data < mini or node.data > maxi:
                return False
            return ( isbst_util(node.left, mini, node.data) and \
                    isbst_util(node.right, node.data+1, maxi))

        return isbst_util(self.root, -(sys.maxsize), sys.maxsize)


    def isbst1(self):
        def isbst1_n2(node):
            if node is None:
                return True
            if node.left is not None and self.minvalue(node.left) > node.data:
                return False
            if node.right is not None and \
                    self.maxvalue(node.right) <= node.data:
                return False
            if not isbst1_n2(node.left) or not isbst1_n2(node.right):
                return False
            return True
        return isbst1_n2(self.root)

    def counttrees(self, numkeys):
        """ For the key values 1...numKeys, how many structurally unique
        binary search trees are possible that store those keys. """
        if numkeys <= 1:
            return 1

        total = 0
        for root in range(1, numkeys+1):
            left = self.counttrees(root - 1)
            right = self.counttrees(numkeys - root)
            total += left * right
        return total

    def sametree(self, bintree):
        """ Given two trees, return true if they are
        structurally identical. """
        def sametreeBT(anode, bnode):
            # both empty -> return true
            if anode is None and bnode is None:
                return True
            # both non-empty compare them
            elif anode is not None and bnode is not None:
                return (anode.data == bnode.data and \
                        sametreeBT(anode.left, bnode.left) and \
                        sametreeBT(anode.right, bnode.right))
            else:
                # one node None other not -> return false
                return False
        return sametreeBT(self.root, bintree.getrootnode())

    def doubletree(self):
        """ For each node in a binary search tree,
        create a new duplicate node, and insert
        the duplicate as the left child of the original node.
        The resulting tree should still be a binary search tree."""
        def doubletreeBT(node):
            if node is None:
                return
            doubletreeBT(node.left)
            doubletreeBT(node.right)
            # duplicate node to left
            oldleft = node.left
            node.left = Node(node.data)
            node.left.left = oldleft
        doubletreeBT(self.root)

    def mirror(self):
        """ Change a tree so that the roles of the
        left and right pointers are swapped at every node."""
        def mirrorBT(node):
            if node is None:
                return
            mirrorBT(node.left)
            mirrorBT(node.right)
            # swap the pointers here
            temp = node.left
            node.left = node.right
            node.right = temp
        mirrorBT(self.root)

    def printpaths(self):
        """Given a binary tree, print out all of its root-to-leaf
        paths, one per line."""
        def printpathsBT(node):
            path = [None] * 1000
            printpathsrecur(node, path, 0)

        def printpathsrecur(node, path, pathlen):
            if node is None:
                return

            path[pathlen] = node.data
            pathlen = pathlen + 1

            # if its a leaf then print the path which led to here
            if (node.left is None) and (node.right is None):
                printList(path, pathlen)
            else:
                printpathsrecur(node.left, path, pathlen)
                printpathsrecur(node.right, path, pathlen)

        def printList(path, pathlen):
            for p in range(pathlen):
                print (path[p], sep=" ", end= " ")
            print ()
        printpathsBT(self.root)


    def haspathsum(self, targetsum):
        """ Given a tree and a sum, return true if there is a path from the root
        down to a leaf, such that adding up all the values along the path
        equals the given sum."""
        def haspathsumBT(node, targetsum):
            if node is None:
                return targetsum == 0
            # lets check both subtress
            return haspathsumBT(node.left, targetsum - node.data) or \
                haspathsumBT(node.right, targetsum - node.data)
        return haspathsumBT(self.root, targetsum)

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

    def minvalue(self, root=None):
        def minvalbst(node):
            if node is None:
                return None
            while node.left is not None:
                node = node.left
            return node.data

        if root is None:
            root = self.root
        return minvalbst(root)

    def maxvalue(self, root=None):
        def maxvalbst(node):
            if node is None:
                return None
            while node.right is not None:
                node = node.right
            return node.data

        if root is None:
            root = self.root
        return maxvalbst(root)

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
