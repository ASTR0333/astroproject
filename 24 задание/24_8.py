with open('24.12.txt') as file:
    s = file.readline().strip()

for k in range(0,100):
    for t in '12349':
        s = s.replace('-0' + k * '0' + t, '-0_' + t)
        s = s.replace('*0' + k * '0' + t, '*0_' + t)

    s = s.replace('-0' + k * '0' + '0-', '-0_0-')
    s = s.replace('-0' + k * '0' + '0*', '-0_0*')
    s = s.replace('*0' + k * '0' + '0-', '*0_0-')
    s = s.replace('*0' + k * '0' + '0*', '*0_0*')


s = s.replace('--','_')
s = s.replace('-*','_')
s = s.replace('*-','_')
s = s.replace('**','_')

lst = s.split('_')
lst = [x.strip('-*') for x in lst]

print(len(max(lst,key=len)))