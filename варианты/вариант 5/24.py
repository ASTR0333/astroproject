with open('24_20813.txt') as file:
    s = file.readline().strip()

for k in range(0,100):
    for n in '789':
        s = s.replace('-0'+k*'0'+n,'-0_'+n)
        s = s.replace('*0' + k * '0' + n, '-0_' + n)
    s = s.replace('-0'+k*'0'+'0-','-0_0-')
    s = s.replace('-0' + k * '0' + '0*', '-0_0*')
    s = s.replace('*0' + k * '0' + '0-', '*0_0-')
    s = s.replace('*0' + k * '0' + '0*', '*0_0*')

s = s.replace('--','_')
s = s.replace('-*','_')
s = s.replace('*-','_')
s = s.replace('**','_')

lst = s.split('_')
lst = [x.strip('*-') for x in lst]

print(max(lst,key=len))