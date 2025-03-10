def proga():
    c = 0
    s = []

    def r(n, p, t):
        nonlocal c, s
        t.append(n)
        if n == 18:
            if 8 in t and 10 in t:
                c += 1
                s.append(p.copy())
            return
        if len(p) > 10: return
        r(n + 2, p + [1], t.copy())
        r(n * 2, p + [2], t.copy())
        r(n - 1, p + [3], t.copy())

    r(2, [], [])
    return c, s


count, programs = proga()
for p in programs:
    print(p)
print(count)