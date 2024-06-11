A_x1, A_y1, A_x2, A_y2 = map(int, input().split())
B_x1, B_y1, B_x2, B_y2 = map(int, input().split())
M_x1, M_y1, M_x2, M_y2 = map(int, input().split())

A_x1 += 1000
A_y1 += 1000
A_x2 += 1000
A_y2 += 1000
B_x1 += 1000
B_y1 += 1000
B_x2 += 1000
B_y2 += 1000
M_x1 += 1000
M_y1 += 1000
M_x2 += 1000
M_y2 += 1000

data = [[0]*2001 for _ in range(2001)]

for i in range(A_x1, A_x2):
    for j in range(A_y1, A_y2):
        data[i][j] = 1

for i in range(B_x1, B_x2):
    for j in range(B_y1, B_y2):
        data[i][j] = 1

for i in range(M_x1, M_x2):
    for j in range(M_y1, M_y2):
        data[i][j] = 0

result = 0
for i in range(2001):
    for j in range(2001):
        if data[i][j] == 1:
            result += 1

print(result)