import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(root, L, before=-1):
    global dp
    for v in tree[root]:
        if before == v:
            continue
        dfs(v, L, root)

    if root in L:
        for k in tree[root]:
            dp[root] += dp[k]
        dp[root] += 1
    else:
        for k in tree[root]:
            dp[root] += dp[k]


Q = int(input())
for _ in range(Q):
    L = list(map(int, input().split()))
    k = L[0]
    V = L[1:]
    dp = [0] * (N + 1)
    dfs(1, V, -1)
    count = 0
    for v in dp:
        if (1 <= v) and (v <= (k - 1)):
            count += 1
    print(count)
