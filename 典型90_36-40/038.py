from math import gcd

A, B = map(int, input().split())


def lcm(m, n):
    # lcm (least common multiple)(最小公倍数)
    return m // gcd(m, n) * n


ans = lcm(A, B)
if ans > 10 ** 18:
    ans = 'Large'
print(ans)
