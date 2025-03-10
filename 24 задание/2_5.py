with open('301_24.txt') as file:
    s = file.readline().strip()

    count_x=0
    l=0
    r=-1
    ans=-10*10

    while True:
        if count_x<=1000:
            r+=1
            if r == len(s):
                break
            if s[r]=='X':
                count_x+=1
        else:
            if s[l]=='X':
                count_x-=1
            l+=1
        if count_x==1000:
            ans = max(ans,(r-l+1))
print(ans)