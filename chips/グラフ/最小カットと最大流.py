# 燃やす埋める問題に帰着させる
# 最小カットは最大流の問題にも帰着できる
# 最大流に負のコストが入っていたらだめ。全て正にする。
INF = 10 ** 18 + 7
N, W = map(int, input().split())
A = list(map(int, input().split()))

S = N
T = N + 1
edge = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(N):
    keys = list(map(int, input().split()))
    for c in keys[1:]:
        c -= 1
        # 家iからcへ向けてINFにすることでカットできなくする
        edge[i][c] = INF

    edge[S][i] = W
    edge[i][T] = A[i]


come = [False] * (N + 2)


# Ford-Fulkerson法(押し戻しを考える)
# https://qiita.com/tanaka-a/items/fb8d84c44190c7098047
def dfs(S, T, f):
    come[S] = True
    if S == T:
        return f
    for to in range(N + 2):
        if come[to]:
            continue
        if edge[S][to] == 0:
            continue
        tmp = dfs(to, T, min(f, edge[S][to]))
        if tmp > 0:
            # 流せた場合は逆の向きに重みを流す
            # これにより0ではない部分ができるため、流せる経路が増える
            # つまり、家に行くことで、それまでに行かないといけない家が開拓できる
            edge[S][to] -= tmp
            edge[to][S] += tmp
            return tmp
    return 0


def max_flow(S, T):
    global come
    ans = 0
    while 1:
        come = [False] * (N + 2)
        f = dfs(S, T, INF)
        if f == 0:
            return ans
        ans += f


k = max_flow(S, T)
print(sum(A) - k)
