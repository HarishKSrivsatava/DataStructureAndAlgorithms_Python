# class template for BinaryTree
class BinaryTreeTest:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Inorder traversal of tree : left node, root node , right node
    def printBinaryTreeinInorder(self):
        if self.left:
            self.left.printBinaryTreeinInorder()
        print(self.data)
        if self.right:
            self.right.printBinaryTreeinInorder()

    def insertNode(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeTest(data)
                else:
                    self.left = self.insertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeTest(data)
                else:
                    self.right = self.insertNode(data)
            else:
                self.data = data




# Driver code
root = BinaryTreeTest(1)
root.insertNode(2)
root.printBinaryTreeinInorder()