def delit(n):
    ans = [1,n]
    for i in range(2,int((n**0.5))+1):
        if n%i==0:
            ans.append(i)
            if i != n//i:
                ans.append(n//i)
    ans.sort()
    return ans



for n in range(63000000,75000001):
    lstd = delit(n)
    lst_n = [x for x in lstd if x%2!=0]
    if len(lst_n) == 5:
        print(n,lst_n[-1])