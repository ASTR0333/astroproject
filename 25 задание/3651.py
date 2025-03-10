def prost(n):
    if n == 1:
        return 0
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return 0
    return 1


def mnp(n):
    lst =[]
    for d in range(2,int(n**0.5)+1):
        while n%d==0:
            lst.append(d)
            n//=d
    if x!=1:
        lst.append(x)
    return lst

ans=[]
for x in range(378312,446492+1):
    lst1 = mnp(x)
    lst2 = list(set(lst1))
    if len(lst1)==2 and len(lst1)==2:
        ans.append(x)
print(len(ans),min(ans))
