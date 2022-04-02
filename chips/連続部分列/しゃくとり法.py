from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
# しゃくとり法は以下のような時に使えるアルゴリズムです。
# 〇〇を満たす区間 (連続する部分列) のうち、最小or最大の長さを求めよ
# 〇〇を満たす区間 (連続する部分列) を数え上げよ
# しゃくとり法

r, ans, tmp = 0, 0, defaultdict(int)
for l in range(N):
    while r < N and len(tmp) <= K:
        tmp[A[r]] += 1
        r += 1
        if len(tmp) <= K:
            ans = max(ans, r - l)
    if l == r:
        r += 1
    else:
        tmp[A[l]] -= 1
    if tmp[A[l]] == 0:
        tmp.pop(A[l])
print(ans)
