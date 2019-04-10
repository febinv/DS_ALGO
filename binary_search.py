def binarysearch(a,alist):
    left=0
    right=len(alist)-1
    flag=0
    while  left<=right and not flag:
        mid=(left+right)//2
        if a==alist[mid]:
            flag=1
        else:
            if a < alist[mid]:
                right=mid-1
            elif a > alist[mid]:
                left=mid+1
    return flag


print(binarysearch(13,[1,2,3,4,5,6,8,9,10]))