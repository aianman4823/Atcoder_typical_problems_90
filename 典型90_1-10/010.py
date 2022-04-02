N = int(input())
cs = []
ps = []
for _ in range(N):
    c, p = map(int, input().split())
    cs.append(c)
    ps.append(p)


acc_P1 = []
acc_P2 = []
for i in range(N):
    if len(acc_P1) == 0 and cs[i] == 1:
        acc_P1.append(ps[i])
        acc_P2.append(0)
        continue

    if len(acc_P2) == 0 and cs[i] == 2:
        acc_P1.append(0)
        acc_P2.append(ps[i])
        continue

    if cs[i] == 1:
        acc_P1.append(acc_P1[len(acc_P1) - 1] + ps[i])
    else:
        acc_P1.append(acc_P1[len(acc_P1) - 1])

    if cs[i] == 2:
        acc_P2.append(acc_P2[len(acc_P2) - 1] + ps[i])
    else:
        acc_P2.append(acc_P2[len(acc_P2) - 1])


Q = int(input())
Ls = []
Rs = []
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l < 0:
        l = 0
    if r < 0:
        r = 0

    ans_a = 0
    ans_b = 0
    if l - 1 >= 0:
        ans_a = acc_P1[r] - acc_P1[l - 1]
        ans_b = acc_P2[r] - acc_P2[l - 1]
    else:
        ans_a = acc_P1[r]
        ans_b = acc_P2[r]

    print(ans_a, ans_b)
