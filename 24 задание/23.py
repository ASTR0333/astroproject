with open('bI4DufyyF.txt') as file:
    s = file.readline().strip()

# print(s)
s = s.replace('*0','_')
s = s.replace('-0','_')

for x in '*-':
    for y in '*-':
        s = s.replace(x+y,'_')
lst = s.split('_')
lst = [x.strip('*-') for x in lst]
lst = [x.lstrip('0') for x in lst]
lst.sort(reverse=True,key=len)
print(len(max(lst,key=len)))
