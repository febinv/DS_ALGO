class BinaryTree():
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None

def inorder(tree):
    stack=[]
    current=tree
    done=0
    while not done:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if len(stack)>0:
                current=stack.pop()
                print(current.root)
                current=current.right
            else:
                done=1


r=BinaryTree('1')
r.left=BinaryTree('2')
r.right=BinaryTree('3')
r.left.left=BinaryTree('4')
r.left.right=BinaryTree('5')

inorder(r)


