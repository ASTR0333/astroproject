with open('24_17756.txt') as file:
    s = file.readline().strip()
    s = s.replace('++','+_+')
    s = s.replace('**', '*_*')
    s = s.replace('+*', '+_*')
    s = s.replace('*+', '*_+')
    lst = s.split('_')
    print(len(max(lst,key=len)))

