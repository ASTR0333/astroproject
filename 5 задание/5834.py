for n in range(256, 1000000):
    r = n * 16
    if n % 2 == 0:
        r += 15
    for i in range(2):
        z = r
        s = 0
        while z > 0:
            s += z % 16
            z //= 16
        r = r * 16 + s % 16
    s = hex(r)[2:]
    if s.count(min(s)) * 5 == s.count(max(s)):
        print(n)
        break