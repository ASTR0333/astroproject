from fnmatch import *
def delit(n):
    ans = [1,n]
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            ans.append(d)
            if n//d != d:
                ans.append(n//d)
    ans.sort()
    return(ans)


for x in range(500_001,800_000):
    lst = delit(x)
    if fnmatch(str(sum(lst)),'*7?'):
        print(x,sum(lst))

