N, K, P, T = map(int, input().split())
data = [[0]*3 for _ in range(T)]

result = [0] * (N+1)
result[K] = 1

# data 만들기
for i in range(T):
    t, x, y = map(int, input().split())
    data[i][0] = t
    data[i][1] = x
    data[i][2] = y

# data 정렬
data.sort(key = lambda x : (x[0], x[1]))

for i in range(K):
    if result[data[i][1]] == 1:
        result[data[i][2]] = 1
    elif result[data[i][2]] == 1:
        result[data[i][1]] = 1

result = ''.join(map(str, result[1:]))
print(result)