from collections import defaultdict
import heapq

N, M = map(int, input().split())

road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append([b, c])
    road[b].append([a, c])


def daikusutora(edges, start: int):
    que = [(-1, start, -1)]
    heapq.heapify(que)
    dists = [float('inf')] * (N + 1)
    while que:
        dist, now, prev = heapq.heappop(que)
        if dists[now] != float('inf'):
            continue

        if prev == -1:
            dists[now] = 0
        else:
            dists[now] = dist

        for nex, now_nex_dist in edges[now]:
            if dists[nex] != float('inf'):
                continue
            heapq.heappush(que, (dists[now] + now_nex_dist, nex, now))
    return dists


node = daikusutora(road, 0)
node2 = daikusutora(road, N - 1)

print(node)
print(node2)
for k in range(N):
    dik = node[k]
    dnk = node2[k]
    print(dik + dnk)
