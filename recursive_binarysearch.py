def recursive_binarysearch(a,alist):
    if len(alist)==0:
        return 0
    else:
        mid=len(alist)//2
        if a==alist[mid]:
            return 1
        else:
            if a>alist[mid]:
                return recursive_binarysearch(a,alist[mid+1:])
            else:
                return recursive_binarysearch(a,alist[:mid])


print(recursive_binarysearch(13,[1,2,3,4,5,6,8,9,13]))