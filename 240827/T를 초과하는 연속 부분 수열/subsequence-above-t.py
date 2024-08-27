N, t = map(int, input().split())
data = list(map(int, input().split()))

cnt, res = 0, 0

for i in range(N):
    if i == 0:
        cnt = 1
    elif data[i] > t and data[i-1] > t:
        cnt += 1
    else:
        cnt = 1
    res = max(cnt,res)

print(res)