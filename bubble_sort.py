def bubblesort(a):
    length=len(a)-1
    while length>0:
        for i in range(length):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        length-=1
    return a

print(bubblesort([9,8,3,4,5,6,7,1,1,2,15]))