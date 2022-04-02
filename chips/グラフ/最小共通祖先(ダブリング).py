'''
最近共通祖先 LCA
ダブリング
木の座標圧縮
公式解説
https://twitter.com/e869120/status/1391218516129312768
ダブリングによるLCAの求め方
https://algo-logic.info/lca/
'''


import sys

input = sys.stdin.readline


sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
Q = int(input())
query = []
for _ in range(Q):
    K, *V = map(int, input().split())
    query.append((K, V))

'''
木を構築する
ダブリングのために各ノードの深さを求めておく
&
木の座標圧縮のためにDFSで通った順に番号をつけておく
&
1個上の頂点par[0][x]を求めておく
'''
depth = [0] * N  # ノードの深さ
id = [0] * N  # DFSで通った順番
bits = 0  # 全ノードをダブリングで求めるのに2の何乗が必要か
while (1 << bits) < N:
    bits += 1
par = [[-1 for _ in range(N)] for _ in range(bits + 1)]  # par[k][i] := ノードiの2^k乗上のノード
vert_id = 0


def build_tree(pos, pre):
    '''
    pos: 今いるノード
    pre: 前のノード

    posからDFS順に辿る
    '''
    global vert_id
    # 2^0==1個上の祖先を記録
    par[0][pos] = pre
    id[pos] = vert_id
    vert_id += 1
    for i in G[pos]:
        if i == pre:
            continue
        depth[i] = depth[pos] + 1
        build_tree(i, pos)


build_tree(0, 0)

# parの計算(2^k個うえの祖先を計算)
for i in range(1, bits):
    for j in range(N):
        par[i][j] = par[i - 1][par[i - 1][j]]


def lca(va, vb):
    '''
    va, vbの最近共通祖先(LCA)を返す
    '''

    # 高さを揃える
    if depth[va] < depth[vb]:
        va, vb = vb, va
    for i in range(bits - 1, -1, -1):
        if depth[va] - depth[vb] >= 1 << i:
            va = par[i][va]
    if va == vb:
        return va

    # 共通の祖先が一致しない場合
    # 共通祖先が一致しない高さまで更新
    for i in range(bits - 1, -1, -1):
        if par[i][va] != par[i][vb]:
            va = par[i][va]
            vb = par[i][vb]
    # その直前を返せば、自然と、最小共通祖先となる
    return par[0][va]


for q in query:
    k, v = q[0], q[1]
    v = sorted([i - 1 for i in v], key=lambda x: id[x])
    answer = 0
    for i in range(k):
        answer += depth[v[i]]
        answer -= depth[lca(v[i], v[(i + 1) % k])]
    print(answer)
