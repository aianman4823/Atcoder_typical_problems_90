from collections import defaultdict
from itertools import permutations
# 制約が小さいものは全探索
# 1 <= N <= 10のように制約が小さい場合!!!!
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
    check = False
    for i, k in enumerate(v):
        if before == -1:
            before = k
            tmp += A[k][i]
            continue

        if before in uwasa[k]:
            check = True
            break
        before = k
        tmp += A[k][i]
    if check:
        continue
    ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
