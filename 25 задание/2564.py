def delit(n):
    ans = [1,n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            ans.append(i)
            if n//i != i:
                ans.append(n//i)
    ans.sort()
    return ans

for n in range(194455,194501):
    lst = delit(n)
    if len(lst) == 4:
        print(lst[-2],lst[-1])
