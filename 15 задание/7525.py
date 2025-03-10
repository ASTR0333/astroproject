def fg(x):
    if x > 70 and x < 90:
        return 1
    else:
        return 0
def check(a):
    for x in range(1,1000):
        f = (x%a==0) or (fg(x) <= (not x%22==0))
        if f == 0:
            return 0
    return 1

for a in range(1,100):
    if check(a) == 1:
        print(a)

