n, k = map(int, input().split())
data = [0]*100
max_value = 0

for _ in range(4):
    c, l = map(int, input().split())
    max_value = max(max_value, l)
    data[l] += c

result = 0

for i in range(k+1, max_value-k+1):
    cnt = data[i]
    for j in range(1, k+1):
        cnt += data[i+j]
        cnt += data[i-j]
    result = max(result, cnt)

print(result)