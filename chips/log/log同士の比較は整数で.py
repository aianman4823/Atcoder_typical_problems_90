a, b, c = map(int, input().split())

# 典型90の020問題
# logの比較は整数で行うべし
left = a
right = c ** b

if left < right:
    print('Yes')
else:
    print('No')
