N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
# https://atcoder.jp/contests/abc245/editorial/3651

# 多項式の一般的な法則性
# https://qiita.com/sano192/items/1b7a541cacaf426aa434

# Bは大きい方から以下のように計算できます!!!s

# Bを作る
B = [0] * (M + 1)

# i=0~M
for i in range(M + 1):
    # x=A[N-1]B[M-(i-1)]+A[N-2]B[M-(i-2)]+...+A[N-k]B[M-(i-k)]+...A[N-i]B[M]
    x = 0
    # k=1~i
    for k in range(1, i + 1):
        # A[N-k]が存在すれば
        if 0 <= N - k:
            x += A[N - k] * B[M - (i - k)]
        # 存在しなければ
        else:
            # 次のiへ
            break
    # 計算
    B[M - i] = (C[M + N - i] - x) // A[N]

# 答えの出力
print(*B)
