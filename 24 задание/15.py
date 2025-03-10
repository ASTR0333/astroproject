file = open('24.txt')
s = file.readline().strip()

for a in 'ABC':
    for b in 'ABC':
        s = s.replace(a+b,'*_*')
lst = s.split('_')
print(len(max(lst,key=len)))
