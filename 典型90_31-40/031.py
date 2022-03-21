# grundy数(不偏ゲームに利用)
# 0の時必敗局面(後手の勝ち)
# 1以上の時必勝局面(先手の勝ち)
# 遷移方法:遷移できる局面のGrundy数の集合に含まれない最小の非負整数
# いくつかのゲームに分割される場合それらのgrundy数のXORをとったものを全体のGrundy数とす
N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
numB = 51 + 50 * (50 + 1) // 2
grundy = [[0] * numB for _ in range(51)]

for i in range(51):
    for j in range(numB):
        # grundy数の集合で最も最小な非負整数を選択するために用意する
        s = set()
        # 遷移1
        if i >= 1 and i + j < numB:
            s.add(grundy[i - 1][i + j])
        # 遷移2
        for k in range(1, j // 2 + 1):
            s.add(grundy[i][j - k])

        mex = 0
        while True:
            if mex not in s:
                break
            mex += 1
        grundy[i][j] = mex

ans = 0
for i in range(N):
    ans ^= grundy[W[i]][B[i]]
if ans == 0:
    print('Second')
else:
    print('First')
