N = int(input())
A = list(map(int, input().split()))


# 区間dpは区間幅が小さい順に進めていく
dp = [[float('inf')] * (2 * N) for _ in range(2 * N)]
# w = 1
for i in range(2 * N):
    dp[i][i] = 0

# w = 2
for i in range(2 * N - 1):
    dp[i][i + 1] = abs(A[i] - A[i + 1])

# w = 3
# 2飛ばしでforを回すのはi,i+1の2つを除くため
for w in range(3, 2 * N, 2):
    for i in range(2 * N - w):
        l = i
        r = i + w

        dp[l][r] = dp[l + 1][r - 1] + abs(A[l] - A[r])

        for k in range(l + 1, r):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])

print(dp[0][2 * N - 1])
