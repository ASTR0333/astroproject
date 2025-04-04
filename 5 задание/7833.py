def to3(n):
    s = ''
    while n !=0:
        last = str(n%3)
        n = n // 3 
        s =  last + s 
    return s 

ans = 10*10**20
for n in range(10,1000):
    n3 = to3(n)

    if n%2==0:
        n3 = n3 + n3[-2] + n3[-1]
     
    else:
        n3 = n3 + to3(n3.count('1') +  n3.count('2') * 2)
    r = int(n3,3)
    if r < ans: 
        ans = r
        print(ans,n)
    
        

            