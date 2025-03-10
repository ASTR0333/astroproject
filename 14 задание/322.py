for x in range(6,50):
    for y in range(6, 50):
        n1 = 5 * x**0 + 2 * x**1 + 2 * x**2
        n2 = 5 * y**0 + 0 * y**1 + 4 * y**2
        if n1 == n2:
            print(x)
