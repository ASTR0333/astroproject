def cv(n):
    return (n**0.5)%1==0


with open('17.txt') as file:
    lst = [int(s.strip()) for s in file]
    lst1 = [x for x in lst if cv(x)]
    os = max(lst1)*3

ans = []
for i in range(len(lst)-1):
    x,y=lst[i],lst[i+1]
    if ((x*y)**0.5)%1==0:
        if x<=os or y<=os:
            ans.append(int((x*y)**0.5))

ans.sort(reverse=True)
print(len(ans),ans[0]+ans[-1])
