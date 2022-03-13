from collections import defaultdict
N = int(input())

users = defaultdict(list)
for i in range(N):
    s = input()
    users[s].append(i + 1)

ans = []
for key, value in users.items():
    ans.append(min(value))

ans.sort()

for a in ans:
    print(a)
