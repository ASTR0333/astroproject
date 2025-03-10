with open('24.txt') as file:
    s = file.readline().strip()
r = -1
l = 0
ans = 10**5
count_x = 0
count_y = 0
while True:
    if count_x <= 500 and count_y == 0:
        r += 1
        if r == len(s):
            break
        if s[r] == 'X':
            count_x += 1
        if s[r] == 'Y':
            count_y += 1
    else:
        l += 1
        if s[l-1] == 'X':
            count_x -= 1
        if s[l-1] == 'Y':
            count_y -= 1
    if count_y == 0 and count_x >= 500:
        ans = min(ans, r-l+1)
print(ans)