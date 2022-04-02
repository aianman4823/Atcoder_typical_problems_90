import math
from functools import reduce


# 最大公約数 (greatest common divisor)
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


A, B, C = map(int, input().split())

divisor = my_gcd(*[A, B, C])
A //= divisor
B //= divisor
C //= divisor
L = [A, B, C]
ans = 0
for v in L:
    ans += v - 1
print(ans)

# ユークリッドの互除法

# x = syou // y + amari
# y = shou2 // amari + amari2


def euclid(x, y):
    amari = x % y
    _ = x // y
    if amari == 0:
        return y
    return euclid(y, amari)


print(euclid(20, 16))


def extgcd(a, b):
    # Extended Euclidean Algorithm(拡張ユークリッド)
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


from math import gcd


def lcm(m, n):
    # 最小公倍数(L.C.M. ：leastcommon multiple)
    # lcm (least common multiple)(最小公倍数)
    return m // gcd(m, n) * n
# ↑
# ２つの整数の積
# 2 つの整数 𝑎, 𝑏 の積は
# 𝑎𝑏 = 𝑔𝑙
# と表せる。
# ただし
# 𝑔 … 最大公約数
# 𝑙 … 最小公倍数
