from unittest import expectedFailure

with open('IGVcRTjyP.txt') as file:
    s = file.readline().strip()

for k in range(0,100):
    for t in '123456789':
        s = s.replace('+0'+k*'0'+t,'+0_'+t)
        s = s.replace('*0' + k * '0' + t, '*0_' + t)

    s = s.replace('+0' + k * '0' + '0+', '+0_0+')
    s = s.replace('+0' + k * '0' + '0*', '+0_0*')
    s = s.replace('*0' + k * '0' + '0+', '*0_0+')
    s = s.replace('*0' + k * '0' + '0*', '*0_0*')

s = s.replace('++','_')
s = s.replace('+*','_')
s = s.replace('*+','_')
s = s.replace('**','_')

lst = s.split('_')
lst = [x.strip('+*') for x in lst]
####################################

otv = []
for s in lst:
    for i in range(len(s)-100):
        for j in range(i+100,len(s)):
            sr = s[i:j + 1]
            try:
                if eval(sr) == 0:
                    otv.append(sr)
            except:
                pass


otv.sort(reverse=True, key=len)


print(*otv[:20],sep='\n')