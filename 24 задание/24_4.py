with open('24.txt') as file:
    s = file.readline().strip()

L, R = 0, -1
count_RO = 0
answer = 0

while True:
    if count_RO <= 21:
        R += 1
        if R == len(s):
            break

        if (R - L + 1) >= 2 and s[R - 1] + s[R] == 'RO':
            count_RO += 1

        if (R - L + 1) >= 3:
            if s[R - 2] + s[R - 1] + s[R] == 'ORO':
                L = R - 1
                count_RO = 1

        if (R - L + 1) >= 3:
            if s[R - 2] + s[R - 1] + s[R] == 'ROR':
                L = R - 1
                count_RO = 0

    else:
        L += 1
        if s[L - 1] + s[L] == 'RO':
            count_RO -= 1
    if count_RO == 21:
        answer = max(answer, R - L + 1)
print(answer)