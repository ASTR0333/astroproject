def f(n):
    n8  = oct(n)[2:]
    for elem in '1357':
        n8 = n8.replace(elem, '2')
    n8 = n8 + str(n%8)
    r = int(n8,8)
    return r

ans = 0

for i in range(10000,100000):
    n = i
    n = f(n)
    n = f(n)
    if n % 2023 == 0:
        ans += i
print(ans)












