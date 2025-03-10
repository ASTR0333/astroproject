def f(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if str_n[i] <= str_n[i + 1]:
            return 0
    return 1

def h(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if str_n[i] >= str_n[i + 1]:
            return 0

    return 1

def summ(n):
    return sum(int(x) for x in str(n))


ans = []
file = open('17-369.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if f(x)==1]
os = min(aos)
s = summ(os)
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if h(x) + h(y) == 1:
        if not( (x*y)%s):
            ans.append(x+y)
print(len(ans),min(ans))

