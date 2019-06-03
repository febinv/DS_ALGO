def maxsubarray(arr):
    i=0
    j=0
    sum=float("-inf")
    while i<len(arr):
        runningsum=0
        j=i
        while j<len(arr):
            runningsum+=arr[j]
            if runningsum>sum:
                sum=runningsum
            j+=1
        i+=1
    return sum

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))