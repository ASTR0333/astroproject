
def check(a):
    for x in range(1,1000):
        f = ((x%2==0) <= (not(x%5==0))) or ((x+a)>=70)
        if f == 0:
            return 0
    return 1

for a in range(1,1000):
    if check(a) == 1:
        print(a)