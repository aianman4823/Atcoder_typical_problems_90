H, W = map(int, input().split())

if H == 1:
    print(W)
    exit()

if W == 1:
    print(H)
    exit()


syou_h = H // 2
syou_w = W // 2

amari_h = H % 2
amari_w = W % 2

if amari_h != 0:
    syou_h += 1

if amari_w != 0:
    syou_w += 1

print(syou_h * syou_w)
