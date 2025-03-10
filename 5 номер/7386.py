ans = []
for n in range(1,10000):
    n8 = oct(n)[2:]
    n8i = int(n8)
    sum = 0
    while n8i != 0:
        sum = sum + n8i%10
        n8i = n8i // 10
    if sum % 2 == 0:
        n8 = n8[0] + n8 + n8[0]
    else:
        n8 = n8 + n8[-1]
    r = int(n8,8)
    if r<1100:
        ans.append(n)
print(max(ans))



