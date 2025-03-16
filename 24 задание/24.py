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
    lpr = s.split('+')
    ans = ''
    for pr in lpr:
        if pr == '0' or '*0*' in pr or '0*' == pr[:2] or '*0' == pr[-2:]:
            ans+=pr+'+'
            otv.append(ans)
        elif '0*' in pr:
            ans = pr[pr.find('0*'):] + '+'
        elif pr[-1]=='0':
            ans = '0+'
        else:
            ans = ''



otv.sort(reverse=True, key=len)
print(*otv[:20],sep='\n')




