import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
for _ in range(Q):
    b = int(input())
    B.append(b)

A_sorted = sorted(A)
for b in B:
    ind = bisect.bisect_left(A_sorted, b)
    if ind == len(A):
        ind -= 1
    right = abs(b - A_sorted[ind])
    left = None
    if 0 < ind < len(A_sorted):
        left = abs(b - A_sorted[ind - 1])

    if left is not None:
        print(min(left, right))
    else:
        print(right)
