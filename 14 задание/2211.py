def to9(n):
    s = ''
    while n != 0:
        last = n%9
        n = n // 9
        s = str(last) + s
    return  s

s = (729**41-81**16)*(729**15+9**5)
print(to9(s).count('0'))
