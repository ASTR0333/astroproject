def f(x1, x2, c, win):
    if x1 + x2 <= 18:  # Указываем условие окончания игры
        return c in win
    if c > max(win):
        return 0
    # Записываем все возможные ходы
    moves = []
    if x1 > 0:
        moves.append(f(x1 - 1, x2, c + 1, win))
        moves.append(f(x1 // 2, x2, c + 1, win))
    if x2 > 0:
        moves.append(f(x1, x2 - 1, c + 1, win))
        moves.append(f(x1, x2 // 2, c + 1, win))
    if c % 2 != max(win) % 2:
        return any(moves)  # Ходит наш игрок
    else:
        return all(moves)  # Ходит противник

# Так как по условию S+K ≥ 19, то начинаем перебор с 10
for N in range(10, 1000 + 1):  # Перебираем стартовое количество камней в куче
    if f(N, N, 0, [2, 4]) == 1 and f(N, N, 0, [2]) == 0:
        print('№ 21:', N)
