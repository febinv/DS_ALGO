class Deque():
    def __init__(self):
        self.items=[]

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

a=Deque()
print(a.isEmpty())
a.addFront(1)
a.addRear(2)
a.addRear(3)
a.addFront(4)
print(a.removeFront())
print(a.removeRear())
print(a.size())
