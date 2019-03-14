#Binary Tree implementation using List of Lists


def binarytree(r):
    return [r,[],[]]

def insertLeft(r,branch):
    t=r.pop(1)
    if len(t)>1:
        r.insert(1,[branch,t,[]])
    else:
        r.insert(1,[branch,[],[]])
    return r

def insertRight(r,branch):
    t=r.pop(2)
    if len(t)>1:
        r.insert(2,[branch,[],t])
    else:
        r.insert(2,[branch,[],[]])
    return r

def getRootval(root):
    return root[0]

def setRoot(root,val):
    root[0] = val

def getLeftchild(root):
    return root[1]

def getRightchild(root):
    return root[2]


r=binarytree(3)
print(r)
print(insertLeft(r,4))
print(insertLeft(r,5))
print(insertRight(r,6))
print(insertRight(r,7))
l=getLeftchild(r)
print(l)

