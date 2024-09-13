N, K = map(int, input().split())
data = list(map(int, input().split()))

max_sum = 0

for i in range(N-K):
    cnt = 0
    for j in range(i, i+K):
        cnt += data[j]
    if cnt >= max_sum:
        max_sum = cnt
print(max_sum)