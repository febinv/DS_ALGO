class Queue():
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

a=Queue()
print(a.isEmpty())
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
print(a.dequeue())
print(a.size())
