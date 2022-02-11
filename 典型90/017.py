N, M = map(int, input().split())
lines = []
for _ in range(M):
    l, r = map(int, input().split())
    lines.append([l, r])


# 小課題1
# ans = 0
# for i in range(M):
#     l1, r1 = lines[i]
#     for j in range(i + 1, M):
#         l2, r2 = lines[j]
#         if l1 < l2 < r1 < r2:
#             ans += 1
#         elif l2 < l1 < r2 < r1:
#             ans += 1

# print(ans)

# 小課題3(余事象 + BIT)
# pattern1: 端点に同じものが含まれる
pattern1 = 0
# どの点から何本線が出ているかを数える
count_list = [0 for _ in range(N + 1)]
for i in range(M):
    l, r = lines[i]
    count_list[l] += 1
    count_list[r] += 1
# 点iにある線分の個数cnt_iから2個線分を選べばOK
for i in range(1, N + 1):
    pattern1 += count_list[i] * (count_list[i] - 1) // 2


pattern2 = 0
v1 = [0 for _ in range(N + 1)]
v2 = [0 for _ in range(N + 1)]
for i in range(M):
    l, r = lines[i]
    v1[r] += 1
    v2[l - 1] += 1

for i in range(1, N + 1):
    v1[i] += v1[i - 1]
    pattern2 += v1[i] * v2[i]


# 右側でソート（小さいものから順に処理するアルゴリズムを利用するため）
# lines.sort(key=lambda x: x[1])を利用すると何かおかしくなる(きちんと新しく作り直して左側に昇順に並べ替えたいものを設置するように)
# vec = []
# for i in range(M):
#     vec.append([lines[i][1], lines[i][0]])
# vec.sort()
# key=lambdaを利用する場合は要素数の順番をきちんと指定してあげる必要がある
lines.sort(key=lambda x: (x[1], x[0]))

# BIT
BIT = [0 for _ in range(N + 1)]


def bit_sum(i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= i & -i
    return s


def bit_add(i, x):
    while i <= N:
        BIT[i] += x
        i += i & -i


pattern3 = 0
for i in range(M):
    l, r = lines[i]
    ret = bit_sum(r) - bit_sum(l)
    pattern3 += ret

    bit_add(l, 1)

total = M * (M - 1) // 2
print(total - pattern1 - pattern2 - pattern3)
