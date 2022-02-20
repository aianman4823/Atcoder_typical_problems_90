from collections import defaultdict
import sys
sys.setrecursionlimit(1000000000)
# 有効グラフに対して「頂点x, yが互いに到達可能なこと」を強連結という
# なお、強連結成分分解(SCC)を使って同じ頂点を1つにまとめると、サイクルを含まないDAGになり、
# 問題によってはこの性質を使うこともあります。
N, M = map(int, input().split())
gragh = defaultdict(list)
r_gragh = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # SCCの準備
    gragh[a].append(b)
    r_gragh[b].append(a)

used = [False] * N
used_r = [False] * N
order = []
# 深さ優先探索(帰りがけ順)


def dfs(root):
    used[root] = True
    for v in gragh[root]:
        if used[v]:
            continue
        dfs(v)
    order.append(root)
    return


def dfs_return(root):
    global cnt
    used_r[root] = True
    for v in r_gragh[root]:
        if used_r[v]:
            continue
        dfs_return(v)
    cnt += 1


for i in range(N):
    if used[i]:
        continue
    dfs(i)

ans = 0
for r_i in reversed(order):
    if used_r[r_i]:
        continue
    cnt = 0
    dfs_return(r_i)
    ans += cnt * (cnt - 1) // 2

print(ans)
