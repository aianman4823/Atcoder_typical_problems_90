from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
N = int(input())
edges = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


# 二部グラフ
# 辺で直接結ばれた頂点同士が互いに違う色になるように、頂点を2色で塗ることができるグラフ
# 性質:
# 1. 奇数長の閉路を含まない
# 2. 最大マッチングが多項式時間で計算できる
leafs = [-1] * N


def dfs(root: int, before: int, color: int):
    global leafs

    if leafs[root] == -1:
        leafs[root] = color
    if color:
        color = 0
    else:
        color = 1
    for v in edges[root]:
        if before == v:
            continue
        dfs(root=v,
            before=root,
            color=color)
    return


dfs(root=0,
    before=-1,
    color=0)


ans1 = []
ans2 = []
count1 = 0
count2 = 0
for i in range(len(leafs)):
    if leafs[i] == 0:
        ans1.append(i + 1)
        count1 += 1
        if count1 == (N // 2):
            break
    else:
        ans2.append(i + 1)
        count2 += 1
        if count2 == (N // 2):
            break

if len(ans1) == (N // 2):
    print(*ans1)
else:
    print(*ans2)
