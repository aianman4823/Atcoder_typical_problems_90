N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort()
# 凸包を求めるアルゴリズムは
# 1. スタックSを用意
# 2. x座標が小さい点から次の操作を行う
# - Sの2番目, 1番目に上の頂点をそれぞれp1, p2, 今見ている点をpaとするとき
# p1p2paが反時計回りではない間、Sをpopすることを繰り返す
# 一連の操作を反時計回りに対しても行うことで、上側凸包、下側凸包両方が求まる

# 時計回りかどうかや反時計回りかどうかは、3点の外積をみることで判断可能です


def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)


# 原点を基準にした外積計算により平行四辺形の面積を得る
# つまり三角形が欲しい場合は2倍になっている
def cross(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def cw(p0, p1, p2):
    pa = (p1[0] - p0[0], p1[1] - p0[1])
    pb = (p2[0] - p0[0], p2[1] - p0[1])
    return cross(pa, pb) > 0


# 凸包のチェックには向きを決めて3点を利用した角度チェックを行う
# クロックワイズ(cw)
convex_hull = []
for p in points:
    while len(convex_hull) >= 2 and cw(convex_hull[-1], convex_hull[-2], p):
        convex_hull.pop()
    convex_hull.append(p)

upper_size = len(convex_hull)
for p in points[-2::-1]:
    while len(convex_hull) > upper_size and cw(convex_hull[-1], convex_hull[-2], p):
        convex_hull.pop()
    convex_hull.append(p)

# 最初と終わりに同じものが2度数えられるから
convex_hull.pop()

n = len(convex_hull)
area2 = 0
inner = 0
outer = 0

for i in range(n):
    now = convex_hull[i]
    # こうすることで、閉じている状況にも対応できる(0に戻るから)
    nxt = convex_hull[(i + 1) % n]
    area2 += cross(now, nxt)
    outer += gcd(abs(now[0] - nxt[0]), abs(now[1] - nxt[1]))

# これ!!!
# 面積 = 内側の面積 + (外側の面積/2) + 1
inner = (area2 - outer + 2) // 2

print(inner + outer - N)
