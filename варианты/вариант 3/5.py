for n in range(100,1000):
    n1 = (n//10%10)*(n//100)
    n2 = (n//10%10)*(n%10)
    if n1 > n2:
        r = str(n1) + str(n2)
    else:
        r = str(n2) + str(n1)
    if r == '123':
        print(n)
