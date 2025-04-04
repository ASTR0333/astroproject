ans = []
for n in range(61,10000):
    n8 = oct(n)[2:]
    if n % 5 == 0:
        n8 = n8 + n8[0] + n8[1] + n8[2]
    else:
        n8 = n8 + bin(n%5)[2:]
    r = int(n8,8)
    if r >= 35000:
        ans.append(n)
print(min(ans))

