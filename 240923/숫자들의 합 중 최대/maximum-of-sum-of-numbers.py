X, Y = map(int, input().split())

result = 0

for cnt in range(X, Y+1):
    cnt_list = list(tuple(map(int, list(str(cnt)))))
    cnt_sum = sum(cnt_list)
    result = max(result, cnt_sum)

print(result)