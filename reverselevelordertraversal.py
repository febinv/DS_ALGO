from collections import deque
class bt:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None


def revordtraversal(root):

    if root is None:
        return None
    stack=[]
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        stack.append(node.data)
    while stack:
        print(stack.pop())

a=bt(10)
a.left=bt(20)
a.right=bt(30)
a.left.left=bt(40)
a.left.right=bt(50)
a.right.left=bt(60)
a.right.right=bt(70)

revordtraversal(a)


