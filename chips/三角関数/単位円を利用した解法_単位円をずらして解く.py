import math
import numpy as np
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for _ in range(Q):
    e = int(input())
    y = -L / 2 * math.sin(math.radians(360 * (e / T)))
    z = L / 2 - L / 2 * math.cos(math.radians(360 * e / T))

    a = math.sqrt(X ** 2 + (y - Y) ** 2)
    b = z

    if a == 0:
        print(0)
        exit()
    print(math.degrees(np.arctan([b / a])))
