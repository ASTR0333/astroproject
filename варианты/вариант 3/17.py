ans = []
file = open('69927.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if abs(x)%32==0]
os = len(aos)
for i in range(len(a)-1):
    x,y=a[i],a[i+1]
    if (x < 0) or (y < 0):
        if (x+y)<os:
            ans.append(x+y)
print(len(ans),max(ans))

