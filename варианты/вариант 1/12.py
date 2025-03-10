def summ(n):
    s = 0
    for i in range(0,len(n)-1):
        s += int(n[i])
    return s


def pr(n):
    for i in range (2,int(n)):
        if int(n)%i == 0:
            return 0
    return 1




for s in range(70 ,10000):
    a = '0' + '1'* s + '2' * s + '0'
    while '00' not in a:
        a = a.replace('02','101',1)
        a = a.replace('11', '2', 1)
        a = a.replace('12', '21', 1)
        a = a.replace('010', '00', 1)
    if pr(summ(a)):
        print(s)

