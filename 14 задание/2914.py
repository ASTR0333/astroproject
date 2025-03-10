ans = []
s = hex(2**51+2**40+2**35+2**17-2**5)[2:]
for i in range(len(s)):
    if s[i] not in ans:
        ans.append(s[i])
print(len(ans))
