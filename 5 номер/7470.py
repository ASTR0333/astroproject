ans = []
def to7(n):
    s = ''
    while n != 0:
        last = n%7
        n = n // 7
        s = str(last) + s
    return s
for n in range(343,2402):
    n7 = to7(n)
    if int(n7[-1]) % 2 == 0:
        n7 = '6' + n7
    else:
        n7 = '5' + n7
    r = int(n7,7)
    if r > 14500:
        ans.append(n)
print(len(ans))

