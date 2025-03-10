def fg(x):
    if x > 15 and x < 40:
        return 1
    else:
        return 0
def fh(x):
    if x > 21 and x < 63:
        return 1
    else:
        return 0

def otr(a1, a2, x):
    if x > a1 and x < a2:
        return 1
    else:
        return 0


def check(a1,a2):
    for x in range(1,1000):
        f = (fg(x)) <= (((fh(x)) and (not otr(a1,a2,x))) <= (not fh(x)))
        if f == 0:
            return 0
    return 1

ans = []
for a1 in range(1,200):
    for a2 in range(1, 200):
        if check(a1,a2) == 1:
            ans.append(a2-a1)
print(min(ans))

