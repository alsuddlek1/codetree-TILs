N = int(input())
data = [0 for i in range(N)]
for i in range(N):
    data[i] = int(input())

cnt, res = 0, 0

for i in range(N):
    if i == 0 :
        cnt = 1
    elif data[i-1] < data[i]:
        cnt += 1
    else:
        cnt = 1
    res = max(cnt, res)

print(res)