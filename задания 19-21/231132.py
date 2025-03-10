def f(x,c,win):
    if 60<=x<=68:
        return c in win
    if x>68:
        return c+1 in win
    if c > max(win):
        return 0
    moves = [f(x+2,c+1,win),f(x+3,c+1,win),f(x*2,c+1,win)]
    if c % 2 != max(win)%2:
        return any(moves)
    else:
        return all(moves)

for s in range(1,60):
    if f(s,0,[3]) == 1 and f(s,0,[1]) == 0:
        print(s)