N = int(input())
ans = list()
i = 1
while i * i <= N:
    if N % i == 0:
        ans.append(i)
        ans.append(N // i)
    i += 1
ans.sort()
print(ans)
