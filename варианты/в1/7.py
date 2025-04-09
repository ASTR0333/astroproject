for p in [x for x in range(1,10**8)]:
    f = 300*300*p*24
    if f<=13*1024*1024*8:
        print(p)