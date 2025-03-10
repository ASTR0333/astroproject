
for n in range(1000,10000):
    n = str(n)
    q = [n[0], n[1], n[2], n[3]]
    mini = sorted(q, reverse=True)
    maks = sorted(q)
    k = mini[0] + mini[1] + mini[2] + mini[3]
    m = maks[0] + maks[1] + maks[2] + maks[3]
    r = int(k) - int(m)
    if r==6174 and int(k) == 9973:
        print(n,k)
#из тестов выяснилось, что макимальный k = 9973




