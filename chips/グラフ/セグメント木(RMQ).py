# RMQ(MはMin または Maxのこと)
# dpとセグメント木を同時に利用し、更新をすばやくさせる技術
class SegTree():
    def __init__(self, init_val, segfunc=max, ide_ele=None):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num

        for i, v in enumerate(init_val):
            self.update(i, v)

    # 更新する場合としない場合がある時の書き方
    def update(self, k, x):
        k += self.num
        while k > 0:
            if self.tree[k] is not None:
                x = self.segfunc(self.tree[k], x)
            if self.tree[k] == x:
                break
            self.tree[k] = x
            k >>= 1
        return

    def query(self, l, r, x):
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                x = self.segfunc(x, self.tree[l])
                l += 1
            if r & 1:
                x = self.segfunc(x, self.tree[r - 1])

            l >>= 1
            r >>= 1

        return x


W, N = map(int, input().split())
foods = []
for _ in range(N):
    L, R, V = map(int, input().split())
    foods.append([L, R, V])

INF = 10**15
dp = [-INF] * (W + 1)
dp[0] = 0
st = SegTree(init_val=dp,
             segfunc=max,
             ide_ele=None)

for i in range(N):
    for w in range(W + 1):
        max_value = st.query(l=max(0, w - foods[i][1]),
                             r=max(0, w - foods[i][0] + 1),
                             x=-INF)
        if max_value > -1:
            dp[w] = max(dp[w], max_value + foods[i][2])

    for i, v in enumerate(dp):
        st.update(i, v)

ans = dp[W]
if ans < 0:
    ans = -1
print(ans)
