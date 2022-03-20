N = int(input())
A = list(range(2, N + 1))
p = list()
while A[0]**2 <= N:
    tmp = A[0]
    p.append(tmp)
    A = [e for e in A if e % tmp != 0]
print(p + A)
