#Return nth to last node 

class Node:
    def __init__(self,value):
        self.value=value
        self.nextnode=None


def nth_to_lastnode(n,node):

        right=node
        left=node
        for i in range(n-1):
            right=right.nextnode

        while right.nextnode:
            left=left.nextnode
            right=right.nextnode

        return left


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e

print(nth_to_lastnode(2,a).value)

