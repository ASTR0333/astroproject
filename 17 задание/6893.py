def t3(n):
    if  '3' in str(n):
        return 1
    else:
        return 0


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

file = open('17-386.txt')
a = [int(s.strip()) for s in file]

ans = []

for i in range(len(a)-2):
    x,y,z = a[i],a[i+1],a[i+2]
    if t3(x) + t3(y) + t3(z) == 3:
        if is_prime(x+y+z):
            ans.append(x+y+z)
print(len(ans),min(ans))


