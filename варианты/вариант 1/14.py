def to8(n):
    s = ''
    while n!=0:
        last = n%8
        s = str(last) + s
        n //=8
    return s



s = 7*512**1912+6*64**1954-5*8**1991-4*8**1980-2022

print(to8(s).count('7'))
