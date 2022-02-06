n = int(input())

answers = []
for i in range(1 << n):
    ans = ''
    branket = 0
    for j in range(n):
        if (i >> j) % 2 == 1:
            ans += '('
        else:
            ans += ')'

    check = True
    for a in ans:
        if a == '(':
            branket += 1
        else:
            branket -= 1
        if branket < 0:
            check = False
            break

    if check and branket == 0:
        answers.append(ans)

answers.sort()
for a in answers:
    print(a)
