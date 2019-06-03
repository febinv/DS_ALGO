def checkpermutation(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        return sorted(str1)==sorted(str2)


print(checkpermutation('febin','nibef'))
print(checkpermutation('febi','ibef'))
