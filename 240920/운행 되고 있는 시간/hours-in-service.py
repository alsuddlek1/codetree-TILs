import sys
MAX_INT = sys.maxsize
N = int(input())
data = []


for _ in range(N):
    x,y = map(int, input().split())
    data.append((x,y))


result = 0
# 1. 한명씩 제외하면서 비교
for i in range(N):
    matrix = [0] * 1001
    for j in range(N):
        # i 번째를 제외하고 비교
        if i==j:
            continue
        start, end = data[j]
        
        for k in range(start, end):
            matrix[k] = 1
    # i번을 제외했을 때 1 채워진 갯수
    cnt = 0

    for l in range(1001):
        if matrix[l] == 1:
            cnt += 1
    result = max(result, cnt)

print(result)