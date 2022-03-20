N, K = map(int, input().split())

# エラトステネスの篩(約数の個数を求める)
cnt_prime = [0] * (N + 1)
for i in range(2, N + 1):
    if cnt_prime[i] == 0:
        x = i
        while x <= N:
            cnt_prime[x] += 1
            x += i
ans = sum([1 if cnt_prime[i] >= K else 0 for i in range(N + 1)])
print(ans)
