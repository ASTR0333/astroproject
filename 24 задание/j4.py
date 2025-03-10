s = '012537'
for c in '02468':
    s = s.replace(c,'*')
for nc in '13579':
    s = s.replace(nc,'#')
while '*#' in s or '#*' in s:
    s = s.replace('*#','*_#')
    s = s.replace('#*','#_*')

lst = s.split('_')
print(lst)


