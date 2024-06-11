N = int(input())

data = [[0]*201 for _ in range(201)]
for _ in range(N):
    x, y = map(int, input().split())
    x += 100
    y += 100

    for i in range(x, x+8):
        for j in range(y, y+8):
            data[i][j] += 1

result = 0
for i in range(201):
    for j in range(201):
        if data[i][j] >= 1:
            result += 1

print(result)