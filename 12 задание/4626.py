k = 0
sr = []
for p1 in range(2,100):
    s = p1*'5'
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    if s not in sr:
        sr.append(s)
        k+=1
print(k)





