def selectionsort(a):
    length=len(a)
    for j in range(0,length-1):
        min=j
        for i in range(j+1,length):
            if a[i]<a[min]:
                min=i
        a[j],a[min]=a[min],a[j]
    return a

print(selectionsort([13,12,4,2,5,6,7,2,1,6,4,3]))