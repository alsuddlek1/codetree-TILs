n, k = map(int, input().split())
data = [0]*101

for _ in range(n):
    c, l = map(int, input().split())
    data[l] += c

result = 0

if k < 50:
    print(1234343)
    for i in range(k+1, 100-k):
        cnt = data[i]
        for j in range(1, k+1):
            cnt += data[i+j]
            cnt += data[i-j]
        result = max(result, cnt)
else:
    result = sum(data)

print(result)