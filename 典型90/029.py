# いもす法では離散的な積み立てはできない
# 区間最大や区間に加算、引算を行う場合はセグメント木を考えよう(遅延セグメント木を利用すれば、区間の更新を一括でできる)


# 小課題1: 単純につむ
# renga = []
# for _ in range(N):
#     l, r = map(int, input().split())
#     l -= 1
#     renga.append([l, r])

# height = [0] * (W + 1)
# for i in range(N):
#     l, r = renga[i]
#     for j in range(l, r):
#         height[j] += 1
#     max_height = max(height[l:r])
#     for j in range(l, r):
#         height[j] = max_height

#     print(max(height[l:r]))

# 小課題2: 座標圧縮

# dic = defaultdict(int)
# renga_old = []
# seq_renga = []
# for _ in range(N):
#     l, r = map(int, input().split())
#     renga_old.append([l, r])
#     seq_renga.append(l)
#     seq_renga.append(r)

# seq_renga = list(set(seq_renga))
# seq_renga.sort()

# for i in range(len(seq_renga)):
#     dic[seq_renga[i]] = i

# renga = []
# for l, r in renga_old:
#     l = dic[l]
#     r = dic[r] + 1
#     renga.append([l, r])


# height = [0] * (W + 1)
# for i in range(N):
#     l, r = renga[i]
#     for j in range(l, r):
#         height[j] += 1
#     max_height = max(height[l:r])
#     for j in range(l, r):
#         height[j] = max_height

#     print(max(height[l:r]))

# 小課題3: 遅延セグメント木(区間の更新にこれを使う。1つの要素のみの更新にはただのセグメント木を利用。)

def segfunc(x, y):
    return max(x, y)


class LazySegTree_RUQ:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l, r):
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v

    def update(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.tree[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


w, n = map(int, input().split())
st = LazySegTree_RUQ([0] * w, segfunc, -10**10)
for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ma = st.query(l, r + 1)
    print(ma + 1)
    st.update(l, r + 1, ma + 1)
