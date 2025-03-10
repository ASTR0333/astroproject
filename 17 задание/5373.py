file = open('17-339.txt')
a = [int(s.strip()) for s in file]

aos = [x for x in a if x>0 and x%19==0]
os = min(aos)


ans = []
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if x+y < os:
        ans.append(x+y)
print(len(ans),max(ans))




