for n in range(100,999):
    ns = str(n)
    a = int(ns[0]) * int(ns[1])
    b = int(ns[1]) * int(ns[2])
    perv = str(max(a,b))
    ans = perv + str(b)
    if ans == '240':
        print(n)

