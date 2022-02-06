# mod = 10 ** 9 + 7
# N = int(input())
# S = input()
# ans = 'atcoder'

# dp = [[0] * (len(ans) + 1) for _ in range(N + 1)]
# for i in range(N + 1):
#     dp[i][0] = 1

# for i in range(N):
#     for j in range(len(ans)):
#         if S[i] == ans[j]:
#             dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
#             dp[i + 1][j + 1] %= mod
#         else:
#             dp[i + 1][j + 1] = dp[i][j + 1]
#             dp[i + 1][j + 1] %= mod


# print(dp)
# a = dp[N][len(ans)] % mod

# print(a)


N = int(input())
S = input()
mod = 10 ** 9 + 7
atcoder = "atcoder"
dp = [[0] * (len(atcoder) + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(len(atcoder)):
        dp[i + 1][j] += dp[i][j]
        if S[i] == atcoder[j]:
            dp[i + 1][j + 1] += dp[i][j]

    for j in range(len(atcoder)):
        dp[i + 1][j] %= mod

print(dp)
# print(dp)
print(dp[N][len(atcoder)] % mod)
