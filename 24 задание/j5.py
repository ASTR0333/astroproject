s = 'FFFAILLLL'
for i in 'FAIL':
    for g in 'FAIL':
        if i != g:
            s = s.replace(i+g,i+'_'+g)
lst = s.split('_')
print(len(max(lst,key=len)))
