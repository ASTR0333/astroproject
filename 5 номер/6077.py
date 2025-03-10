def f(x,y):
    a = x//100 + y//100
    b = x//10 % 10 + y//10 % 10
    c = x%10 + y%10
    return int(str(c) + str(a) + str(b)) //10 %1000
for x in range(100,1000):
    for y in range(100, 1000):
        if f(x,y) == 2:
            print(x,y)