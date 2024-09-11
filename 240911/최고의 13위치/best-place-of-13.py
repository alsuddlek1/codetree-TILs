N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
res = 0
cnt = 0

for i in range(N):
    for j in range(N-2):
        cnt += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        res = max(res, cnt)
        cnt = 0
print(res)