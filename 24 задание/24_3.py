with open('24var07.txt') as file:
    s = file.readline().strip()

L, R = 0, -1
count_AB = 0
ans = 10**10

while True:
    if count_AB < 21:
        R += 1
        if R == len(s):
            break
        if (R - L + 1) >= 2 and s[R-1] + s[R] == 'AB':
            count_AB += 1
    else:
        L += 1
        if s[L-1] + s[L] == 'AB':
            count_AB -= 1
    if count_AB == 21:
        ans = min(ans, R - L + 1)
print(ans)