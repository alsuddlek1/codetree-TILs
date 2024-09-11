N = int(input())
arr = list(map(int, input().split()))

min_sum = 10000
min_cnt = 0
for i in range(N):
    # i = 0,1,2,3,4
    for j in range(N):
        # j = 0,1,2,3
        min_cnt += arr[j] * abs(i-j)
    # print(min_cnt)
    min_sum = min(min_cnt, min_sum)
    min_cnt = 0

print(min_sum)