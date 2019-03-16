class BinaryTree():
    def __init__(self,root):
        self.key=root
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newnode):
        if self.leftChild == None:
            self.leftChild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newnode):
        if self.rightChild == None:
            self.rightChild=BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getrightChild(self):
        return self.rightChild

    def getleftChild(self):
        return self.leftChild

    def setRootval(self,root):
        self.key=root

    def getRootval(self):
        return self.key


r=BinaryTree('a')
print(r.getRootval())
r.insertLeft('b')
print(r.getleftChild().getRootval())
r.insertRight('c')
print(r.getrightChild().getRootval())