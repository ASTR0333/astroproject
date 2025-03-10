def delit(n):
    ans = [1,n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            ans.append(i)
            if n//i != i:
                ans.append(n//i)
    ans.sort()
    return ans

k =[]
maks = -10**20
for n in range(268220,270336):
    lst = delit(n)
    if len(lst) <= 4:
        s = sum(lst)
        if s>maks:
            maks = s
            k = lst
print(sum(k),len(k))





