N, Q = map(int, input().split())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append([x, y])


# f:(x,y)→(x−y,x+y)という写像
# 座標回転(これにより、正方形で考えることができる)
# https://twitter.com/e869120/status/1391886390091075586/photo/1
# マンハッタン距離は45度回転させて考える(回転後はチェビシェフの距離)

rotated_P_X = []
rotated_P_Y = []
for i in range(N):
    x, y = P[i]
    X = x - y
    Y = x + y
    rotated_P_X.append(X)
    rotated_P_Y.append(Y)

X_min = min(rotated_P_X)
X_max = max(rotated_P_X)
Y_min = min(rotated_P_Y)
Y_max = max(rotated_P_Y)

for _ in range(Q):
    q = int(input())
    q -= 1
    base_X = rotated_P_X[q]
    base_Y = rotated_P_Y[q]
    print(max(abs(base_X - X_min), abs(base_X - X_max), abs(base_Y - Y_min), abs(base_Y - Y_max)))
