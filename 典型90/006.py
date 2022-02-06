# # 第6問:水diff O(|S|L) (L=26:アルファベット数)
# N, K = map(int, input().split())
# S = input()
# c = [dict() for i in range(N)]
# d = dict()
# for i in range(N)[::-1]:
#     d[S[i]] = i
#     for j in "abcdefghijklmnopqrstuvwxyz":
#         if j in d:
#             c[i][j] = d[j]
#         else:
#             c[i][j] = N
# ans = []
# i = 0
# while True:
#     for j in "abcdefghijklmnopqrstuvwxyz":
#         if len(ans) + N - c[i][j] >= K:
#             ans.append(j)
#             i = c[i][j] + 1
#             break
#     if len(ans) == K:
#         break
# print("".join(ans))

from collections import defaultdict
import string

lalphabet = string.ascii_lowercase
N, K = map(int, input().split())
S = input()

table = [defaultdict() for _ in range(N)]
d = defaultdict(int)

for i in range(len(S) - 1, -1, -1):
    d[S[i]] = i
    for a in lalphabet:
        if a in d:
            table[i][a] = d[a]
        else:
            table[i][a] = N

ans = []
i = 0
while 1:
    for a in lalphabet:
        if len(ans) + N - table[i][a] >= K:
            ans.append(a)
            i = table[i][a] + 1
            break

    if len(ans) == K:
        break
print("".join(ans))
# ans = []
# i = 0
# while True:
#     for j in "abcdefghijklmnopqrstuvwxyz":
#         if len(ans) + N - c[i][j] >= K:
#             ans.append(j)
#             i = c[i][j] + 1
#             break
#     if len(ans) == K:
#         break
# print("".join(ans))
