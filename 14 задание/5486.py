for x in range(19):
    n1 = 6*19**0 + 3*19**1 + x*19**2 + 5*19**3 + 5*19**4
    n2 = 4*19**0 + 2*19**1 + 7*19**2 + 2*19**3 + x*19**4
    s = n1+n2
    if s%11==0:
        print(s//11)