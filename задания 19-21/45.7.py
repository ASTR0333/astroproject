def f(x, c, win):
    if x == 42:  #
        return c in win
    if c > max(win):
        return 0
    if x < 42:
        moves = [f(x + 1, c + 1, win), f(x + 3, c + 1, win), f(x + 7, c + 1, win)]
    else:
        moves = [f(x - 1, c + 1, win), f(x - 3, c + 1, win), f(x - 7, c + 1, win)]


