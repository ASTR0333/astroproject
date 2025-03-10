def last(n):
    last_two_digits = abs(n) % 100
    tens = last_two_digits // 10
    units = last_two_digits % 10
    return tens == units




ans = []
file = open('17-354.txt')
a = [int(s.strip()) for s in file]
aos = [x for x in a if last(x)]
os = sum(aos)/len(aos)
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (((abs(x)%100)//10) == (abs(y)%10)) or (((abs(y)%100)//10) == (abs(x)%10)):
        if (abs(x)%11==0) + (abs(y)%11==0) == 1:
            if x**2 + y**2 >= os**2:
                ans.append(x**2+y**2)
print(len(ans))
print(max(ans))
