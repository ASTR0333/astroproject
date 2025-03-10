with open('24-295.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_DE = 0
ans = -1
while True:
    if count_DE <= 240:
        r += 1
        if r == len(s):
            break
        if r-l+1 >= 2 and s[r-1] + s[r] == 'DE':
            count_DE += 1
    else:
        l += 1
        if s[l-1] + s[l] == 'DE':
            count_DE -= 1
    if count_DE <= 240:
        ans = max(ans, r-l+1)
print(ans)