s1 = 30
s2 = s1+12
s3 = 24+s2
s4 = 23
s5 = 33
s6 = 47
s7 = 28 + max(s2,s5)
s8 = 15 + max(s4,s6)
s9 = 15
s10 = 45 + max(s3,s7,s9)
s11 = 13
s12 = 16 + max(s10,s11)
s14 = 15
s15 = 21
s16 = 45+max(s2,s7,s8)
s17 = 44+max(s12,s14)
s18 = 45
s19 = 32+max(s17,s18)
for t in range(1,1000):
    s13 = t + max(s4,s10)
    l = max(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19)
    if l == 220:
        print(t)
