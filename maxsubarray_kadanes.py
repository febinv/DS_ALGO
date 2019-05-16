def maxsubarray_kadanes(arr):
    maxsofar=arr[0]
    maxendinghere=arr[0]
    i=1
    while i<len(arr):
        if (maxendinghere+arr[i]) > arr[i]:
            maxendinghere=maxendinghere+arr[i]
        else:
            maxendinghere=arr[i]

        if maxsofar<maxendinghere:
            maxsofar=maxendinghere
        i+=1
    return maxsofar

print(maxsubarray_kadanes([-2,1,-3,4,-1,2,1,-5,4]))