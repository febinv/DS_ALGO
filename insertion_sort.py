def insertionsort(a):
    length=len(a)
    for i in range(1,length):
        key=i
        while key>0:
            if a[key]<a[key-1]:
                a[key],a[key-1]=a[key-1],a[key]
            key-=1
    return a

print(insertionsort([12,11,10,9,8,7,6,5,4,3,2,1]))
