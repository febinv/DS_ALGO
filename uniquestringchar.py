def uniquestringchar(n):
    check={}
    mylist=[]
    for i in range(len(n)):
        if n[i] not in check:
            check[n[i]]=1
        else:
            mylist.append(n[i])
    if len(mylist)!=0:
        return 1
    else:
        return 0

def uniquestringchar_n2soln(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i]==n[j] and i!=j:
                return 1
    return 0

print(uniquestringchar("palindrome"))
print(uniquestringchar("palindromep"))
print(uniquestringchar_n2soln("palindrome"))
print(uniquestringchar_n2soln("palindromep"))