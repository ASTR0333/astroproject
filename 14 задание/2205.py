def to9(n):
    s = ''
    while n != 0:
        last = n%9
        n = n // 9
        s = str(last) + s
    return  s

s = 5*6561**46 + 5*729**15 - 5*5832 - 5
print(to9(s).count('4'))
