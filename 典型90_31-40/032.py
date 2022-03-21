from collections import defaultdict
from itertools import permutations
# 制約が小さいものは全探索
N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

M = int(input())
uwasa = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uwasa[x].append(y)
    uwasa[y].append(x)

ans = float('inf')
for v in permutations(range(0, N)):
    tmp = 0
    before = -1
    for i, k in enumerate(v):
        if before == -1:
            before = k
            tmp += A[k][i]
            O
        tmp += A[k][i]

    ans = min(ans, tmp)

print(ans)
