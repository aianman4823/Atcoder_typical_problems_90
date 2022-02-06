H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)


row_sum = []
for a in A:
    row_sum.append(sum(a))

columns_sum = []
for i in range(W):
    sum_ = 0
    for j in range(H):
        sum_ += A[j][i]
    columns_sum.append(sum_)


for i in range(H):
    tmp = []
    for j in range(W):
        tmp.append(row_sum[i] + columns_sum[j] - A[i][j])
    print(*tmp)
