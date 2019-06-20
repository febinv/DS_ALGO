class Node:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None


prev=float('-inf')
def inorder(root):
    global prev
    if root is None:
        return None
    else:
        inorder(root.left)
        if prev is not None and prev>root.root:
            return 1
        prev=root.root
        inorder(root.right)

def isbst(root):
    ans=inorder(root)
    if ans:
        print("not BST")
    else:
        print("BST")



a=Node(4)
a.left=Node(2)
a.right=Node(5)
a.left.left=Node(1)
a.left.right=Node(3)
#a.right.left=Node(7)
#a.right.right=Node(8)

isbst(a)