a, b, c = map(int, input().split())

# logの比較は整数で行うべし
left = a
right = c ** b

if left < right:
    print('Yes')
else:
    print('No')
