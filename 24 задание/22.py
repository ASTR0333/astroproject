with open('In7Bbmjp3.txt') as file:
    s = file.readline().strip()

s = s.replace('++','_')
lst = s.split('_')
lst = [x.strip('+') for x in lst ]
lst = [x for x in lst if '+' in x]
lst.sort(reverse=True,key=len)
print(len(max(lst,key=len)))