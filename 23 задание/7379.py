def f(x,end,f8,f16,f32):
    if x == 8:
        f8 = 1
    if x == 16:
        f16 = 1
    if x == 32:
        f32 = 1
    if x > end:
        return 0
    if x == end and (f8 + f16 + f32 == 1):
        return 1
    return f(x+1,end,f8,f16,f32)+f(x+4,end,f8,f16,f32)+f(x*2,end,f8,f16,f32)


print(f(1,50,0,0,0))
