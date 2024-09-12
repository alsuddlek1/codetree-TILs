N, S = map(int, input().split())
data = list(map(int, input().split()))
reset = data
result = S

for i in range(N-1):
    for j in range(i+1, N):
        data[i], data[j] = 0, 0
        cnt = 0
        for k in range(N):
            cnt += data[k]
        if abs(S - cnt) <= result:
            result = abs(S - cnt)
        data = reset

print(result)