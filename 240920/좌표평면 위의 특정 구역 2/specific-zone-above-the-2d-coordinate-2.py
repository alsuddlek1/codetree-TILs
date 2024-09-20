N = int(input())

data = []

for _ in range(N):
    x,y = map(int, input().split())
    data.append((x,y))

result = 100000000 # 사각형 넓이

# 1. 점 하나씩 제외
for i in range(N):
    x1, x2, y1, y2 = 0, 40000, 0, 40000
    for j in range(N):
        if i == j:
            continue
        # 나머지 점 중 x1-x2 * y1-y2 비교
        x1 = max(x1, data[j][0])
        x2 = min(x2, data[j][0])
        y1 = max(y1, data[j][1])
        y2 = min(y2, data[j][1])
    result = min(result, (x1-x2)*(y1-y2))

print(result)