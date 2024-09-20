import sys
MAX_INT = sys.maxsize

N = int(input())
data = []
for _ in range(N):
    x,y = map(int, input().split())
    data.append((x,y))

result = 0

# 1. 점 세개씩 비교
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 2. 세 개중 x/y가 각각 두개 같아야함
            if (data[i][0] == data[j][0] or data[i][0] == data[k][0] or data[j][0] == data[k][0]) and (data[i][1] == data[j][1] or data[i][1] == data[k][1] or data[k][1] == data[j][1]):
                
                if data[i] == data[j] or data[i] == data[k] or data[j] == data[k]:
                    continue
                else:
                    x1 = max(data[i][0], data[j][0], data[k][0])
                    x2 = min(data[i][0], data[j][0], data[k][0])
                    y1 = max(data[i][1], data[j][1], data[k][1])
                    y2 = min(data[i][1], data[j][1], data[k][1])
                    # 삼각형 넓이 *2
                    S = abs(x1-x2) * abs(y1-y2)
                    result = max(result, S)
print(result)