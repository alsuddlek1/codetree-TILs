N, K = map(int, input().split())
max_cnt = 0
data = [0]*10000


## data 만들기
for _ in range(N):
    roc, soc = input().split()
    roc = int(roc)
    max_cnt = max(max_cnt, roc)
    if soc == "G":
        data[roc] = 1
    elif soc == "H":
        data[roc] = 2
# print(data)

## 계산
max_sum = 0
for i in range(1, 10000-K):
    # print(i)
    cnt = 0
    for j in range(i, i+K+1):
        # print(j)
        cnt += data[j]
        # print(j, cnt)

    max_sum = max(max_sum, cnt)

print(max_sum)