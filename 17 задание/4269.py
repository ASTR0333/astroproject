k = 0
ans = []
with open('17-1.txt') as file:
    a = [int(s.rstrip()) for s in file]
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (x%7==0 and y%17 != 0) or (y%7==0 and x%17 != 0):
        k+=1
        ans.append(x+y)
print(k)
print(min(ans))