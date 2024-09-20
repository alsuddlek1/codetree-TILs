import sys
MAX_INT = sys.maxsize

N = int(input())
data = []
for _ in range(N):
    x,y = map(int, input().split())
    data.append((x,y))

result = MAX_INT

# 1. 점 두개씩 모든 경우 탐색
for i in range(N):
    x1, x2, y1, y2 = 0, 0, 0, 0
    for j in range(i+1, N):
        x1 = data[i][0]
        x2 = data[j][0]
        y1 = data[i][1]
        y2 = data[j][1]
    
        # 2. 거리 비교
        leng = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
        result = min(result, leng)

print(result)