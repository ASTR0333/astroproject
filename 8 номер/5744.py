

def prime(n):
    if n <= 1:
        return 0
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1
ans = 0
for p1 in '123456':
    for p2 in '0123456':
        for p3 in '0123456':
            for p4 in '0123456':
                for p5 in '0123456':
                    s = p1 + p2 + p3 + p4 + p5
                    summ = int(p1) + int(p2) + int(p3) + int(p4) + int(p5)
                    if s.count('0') + s.count('2') + s.count('4')+ s.count('6') >=3:
                        if prime(summ) == 1:
                            ans += 1
print(ans)