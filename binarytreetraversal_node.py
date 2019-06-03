class BinaryTree():
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None



r=BinaryTree('a')
r.left=BinaryTree('b')
r.right=BinaryTree('c')
r.left.left=BinaryTree('d')
r.left.right=BinaryTree('e')
r.right.left=BinaryTree('f')
r.right.right=BinaryTree('g')

def preorder(tree):
    if tree is not None:
        preorder(tree.left)
        print(tree.root)
        preorder(tree.right)


preorder(r)


