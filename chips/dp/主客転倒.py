# 主客転倒
# コストの寄与を考える
# 答えへの貢献度を考えた上で木DPを行う
# https://twitter.com/e869120/status/1392974101061378049/photo/1
import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dp = [0] * (N + 1)


def dfs(root, pre=-1):
    dp[root] = 1
    for v in edges[root]:
        if pre != v:
            dfs(v, pre=root)
            dp[root] += dp[v]


dfs(root=0)

ans = 0
for u in range(N):
    ans += dp[u] * (N - dp[u])

print(ans)
