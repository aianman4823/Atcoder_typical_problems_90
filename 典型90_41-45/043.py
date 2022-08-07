from collections import deque

H, W = map(int, input().split())

rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1
cs -= 1
rt -= 1
ct -= 1

grids = []
for _ in range(H):
    s = input()
    grids.append(s)

INF = 10 ** 6
dp = [[INF] * W for _ in range(H)]
dp[rs][cs] = 0

que = deque()
que.append((rs, cs))

mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while que:
    rq, cq = que.popleft()
    for x, y in mov:
        rtmp, ctmp = rq, cq
        while True:
            rtmp += x
            ctmp += y
            if not (0 <= rtmp < H and 0 <= ctmp < W):
                break
            if grids[rtmp][ctmp] == "#":
                break
            if dp[rtmp][ctmp] < dp[rq][cq] + 1:
                break
            elif dp[rtmp][ctmp] > dp[rq][cq] + 1:
                dp[rtmp][ctmp] = dp[rq][cq] + 1
                que.append((rtmp, ctmp))

print(dp)
ans = max(0, dp[rt][ct] - 1)
print(ans)
