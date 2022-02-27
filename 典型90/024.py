N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = []
for i in range(N):
    diff.append(abs(A[i] - B[i]))

if sum(diff) > K:
    print('No')
    exit()

if K % 2 == sum(diff) % 2:
    print('Yes')
else:
    print('No')
