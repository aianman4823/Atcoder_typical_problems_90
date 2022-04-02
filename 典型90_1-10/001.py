K, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def solve(mid):
    cnt = 0
    pre = 0
    for a in A:
        if (a - pre) >= mid and (L - a) >= mid:
            cnt += 1
            pre = a
    if cnt >= K:
        return True
    else:
        return False


left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    b = solve(mid)
    if b:
        left = mid
    else:
        right = mid

print(left)
