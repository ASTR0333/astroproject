def f(x,c,win):
    if x > 99:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x+1,c+1,win),f(x**2,c+1,win)]
    if c%2 != max(win)%2:
        return any(moves)
    else:
        return all(moves)
for s in range(1,99):
    if f(s,0,[2,4]) == 1 and f(s,0,[2]) == 0:
        print(s)