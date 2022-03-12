import sys
sys.setrecursionlimit(10 ** 6)
N, B = map(int, input().split())

# まとめて考える探索/複雑な構造の全探索は再帰関数
# f(x)が同じものはまとめて考えて良い
Answer = 0


def dfs(pos: int, last: int, str_num: str):
    global Answer

    if pos == 0:
        rem = 1
        for i in range(len(str_num)):
            rem *= int(str_num[i])
        goal = rem + B
        if goal <= N:
            goal_str = str(goal)
            goal_str = sorted(goal_str)
            goal_str = sorted(goal_str, reverse=True)
            goal_str = "".join(goal_str)
            if goal_str == str_num:
                Answer += 1
        return

    for i in range(last, 0, -1):
        str2 = str_num
        str2 += str(i)
        dfs(pos - 1, i, str2)


for i in range(1, 12):
    dfs(i, 9, "")

V = str(B)
flag = False
for i in range(0, len(V)):
    if V[i] == '0':
        flag = True
if flag and N >= B:
    Answer += 1

print(Answer)
