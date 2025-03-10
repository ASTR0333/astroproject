def f(x,c,win):
    if 45<=x<=112:
        return c in win
    if x>112:
        return c+1 in win
    if c>max(win):
        return 0
    moves = [f(x+2,c+1,win),f(x*3,c+1,win)]
    if c%2 != max(win)%2:
        return any(moves)
    else:
        return all(moves)
for s in range(1,45):
    if f(s,0,[2,4]) == 1 and f(s,0,[2]) == 0 :
        print(s)

