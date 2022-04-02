mod = 10 ** 9 + 7
H, W = map(int, input().split())
C = []
for _ in range(H):
    c = input()
    C.append(c)

# 小課題1(bit全探索)
count = 0
for i in range(2 ** (H * W)):
    break_flag = False
    masu = [[0] * W for _ in range(H)]
    ans = []
    h = 0
    for j in range(H * W):
        if j // W > 0 and j % W == 0:
            h += 1
        if ((i >> j) & 1):
            if C[h][j % W] == '.':
                masu[h][j % W] = 1
            else:
                break_flag = True
                break
        else:
            masu[h][j % W] = 0
    if break_flag:
        continue

    flag = True
    for j in range(H):
        for k in range(W):
            if masu[j][k] == 1:
                for mx in range(-1, 2):
                    for my in range(-1, 2):
                        if mx == 0 and my == 0:
                            continue
                        if 0 <= (my + j) < H and 0 <= (mx + k) < W:
                            if masu[my + j][mx + k] == 1:
                                flag = False

    if flag:
        count += 1
        count %= mod

print(count % mod)
