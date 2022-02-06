from collections import defaultdict, deque
import sys
sys.setrecursionlimit(20000)

N = int(input())
roads = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append(b)
    roads[b].append(a)

INF = float('inf')
dfs1_count = [INF] * N


def dfs1(now):
    stack = deque()
    stack.append(now)
    while len(stack):
        p = stack.pop()
        for r in roads[p]:
            if dfs1_count[r] == INF:
                dfs1_count[r] = dfs1_count[p] + 1
                stack.append(r)
    return


dfs1_count[0] = 0
dfs1(0)

max_ind = dfs1_count.index(max(dfs1_count))
dfs1_count = [INF] * N
dfs1_count[max_ind] = 0
dfs1(max_ind)

print(max(dfs1_count) + 1)
