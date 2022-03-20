N = int(input())
i = 2
ans = dict()
div_sum = 1
n = N
while i * i <= N:
    while n % i == 0:
        n = n // i
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    i += 1
if n != 1:
    ans[n] = 1

ans_list = list(ans.items())
for j in ans_list:
    div_sum *= j[1] + 1
print(div_sum)
