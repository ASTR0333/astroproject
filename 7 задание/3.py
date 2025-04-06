wh = 3840*2160
k = 60*90
for n in range(1,1000000):
    f1 = wh*k*n
    f2 = 48000*16*2*90
    f = f1+f2
    if f==(54691875*1024*8):
        print(n)
