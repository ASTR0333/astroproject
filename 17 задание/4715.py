def sch(x):
    summ = 0
    while x!=0:
        last = x%10
        x = x//10
        summ = summ + last

    return summ


file = open('17-243.txt')
a = [int((s.strip())) for s in file]
os = [sch(x) for x in a if x%33==0]
summ = sum(os)

k = 0
ans = []
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if x>summ or y>summ:
        k+=1
        ans.append(x+y)
print(k, min(ans))
