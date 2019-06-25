class bt:
    def __init__(self,root):
        self.val=root
        self.left=None
        self.right=None


def findpath(root,path,n1):
    if root is None:
        return None
    path.append(root.val)
    if root.val==n1:
        return True
    if (findpath(root.left, path, n1) or findpath(root.right, path, n1)):
        return path
    path.pop()
    return False

a=bt(10)
a.left=bt(20)
a.right=bt(30)
a.left.left=bt(40)
a.left.right=bt(50)
a.right.left=bt(60)
a.right.right=bt(70)


print(findpath(a,[],60))


