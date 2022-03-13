from collections import defaultdict
# 二次元いもす法
# 座標で考えて面積に落とす
N = int(input())
A = [[0] * 1100 for _ in range(1100)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    A[lx][ly] += 1
    A[rx][ry] += 1
    A[rx][ly] += -1
    A[lx][ry] += -1

for i in range(1100):
    for j in range(1100):
        if i == 0 and j == 0:
            continue
        A[i][j] = A[i][j] + A[i][j - 1]


for i in range(1100):
    for j in range(1100):
        if i == 0 and j == 0:
            continue
        A[j][i] = A[j][i] + A[j - 1][i]


count = defaultdict(int)
for i in range(1100):
    for j in range(1100):
        count[A[i][j]] += 1

for i in range(N):
    print(count[i + 1])
