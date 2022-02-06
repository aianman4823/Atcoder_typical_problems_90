from typing import List
import math
mod = 10**9 + 7
N = int(input())


def combination(fact: List, n: int, r: int):
    return fact[n] * pow(fact[n - r] * fact[r], mod - 2, mod) % mod


# 1 * 2 * 3 * .....*N
kaijou = [1]
for i in range(N):
    kaijou.append(kaijou[-1] * (i + 1) % mod)

anses = []
for k in range(1, N + 1):
    max_N = math.ceil(N / k)
    ans = 0
    for a in range(1, max_N + 1):
        ans += combination(kaijou, N - (a - 1) * (k - 1), a)
        ans %= mod
    anses.append(ans)

print(*anses, sep='\n')
