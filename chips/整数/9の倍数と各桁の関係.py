mod = 10 ** 9 + 7
K = int(input())

# Xが9の倍数かどうか <=> Xの十進数表記の各桁の合計が9の倍数かどうか
# と同意である

if K % 9 != 0:
    print(0)
    exit()

# dp[s]: 総和がsになる個数
# 最後の桁が1-9のうちどれかで場合分け
# dp[s] = dp[s - 1] + dp[s - 2] + ・・・・・ + dp[s - 9]

dp = [0] * (K + 1)
# 初期化する時、s=0になる通り数は1という初期化に慣れるべし
dp[0] = 1
for s in range(K + 1):
    for i in range(1, 10):
        if s - i < 0:
            continue
        dp[s] += dp[s - i]
        dp[s] %= mod

print(dp[K] % mod)
