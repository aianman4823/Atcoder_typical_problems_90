from collections import defaultdict


d = defaultdict(int)
H, W = map(int, input().split())
Q = int(input())
qs = []
for _ in range(Q):
    q = input()
    qs.append(q)


mw = [0, 1, -1, 0]
mh = [1, 0, 0, -1]



def flatten(h, w):
    # ここで直交座標を一意な数値に変更する必要がある
    ans = h + (H * 1) * w
    return ans


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


M = [False] * ((H + 1) * W)
n = len(M)
uf = UnionFind(n)

for q in qs:
    qseq = q.split()
    if qseq[0] == '1':
        w, h = int(qseq[2]), int(qseq[1])
        w -= 1
        h -= 1
        x = flatten(h, w)
        M[x] = True
        for i in range(4):
            w_dash, h_dash = w + mw[i], h + mh[i]
            y = flatten(h_dash, w_dash)
            if 0 <= h_dash < H and 0 <= w_dash < W:
                if M[y]:
                    uf.union(x, y)
    else:
        wa, ha, wb, hb = int(qseq[2]), int(qseq[1]), int(qseq[4]), int(qseq[3])
        wa -= 1
        ha -= 1
        wb -= 1
        hb -= 1
        x = flatten(ha, wa)
        y = flatten(hb, wb)
        if uf.same(x, y) and M[x] and M[y]:
            print('Yes')
        else:
            print('No')
