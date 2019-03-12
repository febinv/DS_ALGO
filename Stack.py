class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

a=Stack()
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
print(a.peek())
print(a.isEmpty())
print(a.size())