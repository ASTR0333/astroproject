with open('24_2.txt') as file:
    s = file.readline().strip()

alph = 'CDEFGHIJKLMNOPQRSTUVWXYZ'

for x in alph:
    s = s.replace(x,'_')

lst = s.split('_')
lst = [x for x in lst if len(x)!=0]
maks = -10**10
ans = ''
for x in lst:
    for l in range(len(x)):
        for r in range(l+1,len(x)):
            q = x[l:r]
            m = int(q,12)
            if m%6==0 and m>maks:
                maks = m
                ans = q

print(ans)







