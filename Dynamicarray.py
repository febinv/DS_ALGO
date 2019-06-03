from ctypes import py_object

class Dynamicarray():
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)


    def append(self,element):
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n]=element
        self.n+=1

    def _resize(self,new_cap):
        B=self.make_array(new_cap)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=new_cap

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0<=k<self.n:
            return "Out of bounds"
        return self.A[k]

    def make_array(self,new_cap):
        return (new_cap*py_object)()

m=Dynamicarray()
m.append(1)
m.append(2)
m.append(3)
print(len(m))
print(m[2])	