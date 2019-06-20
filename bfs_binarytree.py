class Node:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None



def bfs(root):
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        print(node.root)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)




a=Node(4)
a.left=Node(2)
a.right=Node(3)
a.left.left=Node(5)
a.left.right=Node(6)
a.right.left=Node(7)
a.right.right=Node(8)

bfs(a)