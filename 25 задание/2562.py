def delit(n):
    ans = []
    for i in range(2,int((n**0.5))+1):
        if n%i==0:
            ans.append(i)
            if i != n//i:
                ans.append(n//i)
    ans.sort()
    return ans



for n in range(174457,174506):
    lstd = delit(n)
    if len(lstd) == 2:
        print(lstd)


































#[1,2,3,4,6,12]


