def seqsearch(a,alist):
    pos=0
    flag=False
    while pos<=len(alist)-1:
        if a == alist[pos]:
            flag=True
            break
        pos+=1
    return flag

def orderedseqsearch(a,alist):
    pos=0
    flag=False
    while pos<=len(alist)-1:
        if a == alist[pos]:
            flag=True
            break
        elif a < alist[pos]:
            break
        pos+=1
    return flag

print(seqsearch(1,[4,5,6,7,8,1]))
print(orderedseqsearch(6,[1,2,3,4,5,7,8,9,10]))
