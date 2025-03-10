def mn(n):
    lst = []
    for d in range(2,int(n**0.5)+1):
        while n%d==0:
            lst.append(d)
            n//=d
    if n != 1:
        lst.append(n)
    lst.sort()
    return lst

ch = 0
mins = 10**6
k = 0
for n in range(485617,529678+1):
    lst = mn(n)
    lst1 = list(set(lst))
    s = lst1[0]%10
    lst2 = [x for x in lst1 if x%10==s]
    if len(lst) == 3 and len(lst1) == 3 and len(lst2) == 3:
        k+=1
        if (max(lst2)-min(lst2)) < mins:
            mins = (max(lst2)-min(lst2))
            ch = n
print(k,ch)


