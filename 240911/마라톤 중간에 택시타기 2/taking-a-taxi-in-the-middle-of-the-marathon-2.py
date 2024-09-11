N = int(input())
point = []

for _ in range(N):
    x,y = map(int, input().split())
    point.append((x,y))
res = 100000000
for i in range(1, N-1):
    result = point[:i] + point[i+1:]

    total = 0
    for j in range(N-2):
        x1, y1 = result[j]
        x2, y2 = result[j+1]
        distance = abs(x1-x2) + abs(y1-y2)
        total += distance

    res = min(res, total)
print(res)