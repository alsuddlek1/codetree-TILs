n = int(input())
cnt = 0

data = [[0]*201 for _ in range(201)]

while cnt != n:
    cnt += 1
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            if cnt % 2 == 0: # 홀수일때 blue = 1
                data[i][j] = 1
            else: # 짝수일때 red = 3
                data[i][j] = 3

result = 0
for i in range(201):
    for j in range(201):
        if data[i][j] == 1:
            result += 1

print(result)