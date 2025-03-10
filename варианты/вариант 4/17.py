ans = []
file = open('107_17.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if x%21==0]
os = min(aos)
for i in range(len(a)-1):
    x,y = a[i],a[i+1]
    if x%os == 0 or y%os == 0:
        ans.append(x+y)
print(len(ans),max(ans))

