class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        print(str(data)+" pushed to stack")

    def pop(self):
        if self.head is None:
            print("stack is empty")
            return
        popped=self.head.data
        self.head=self.head.next
        print("popped is :"+str(popped))


stack=LinkedList()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

