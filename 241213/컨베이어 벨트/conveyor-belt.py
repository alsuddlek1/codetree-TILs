# 1. 변수선언
n, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(2)]

# 2. 컨베이너
# 2-1. 첫번째 행 temp

for time in range(t):
    temp = data[0][-1]

    for i in range(n-1, 0, -1):
        data[0][i] = data[0][i-1]

    data[0][0] = data[1][-1]

    for i in range(n-1, 0, -1):
        data[1][i] = data[1][i-1]

    data[1][0] = temp

for i in range(2):
    for j in range(n):
        print(data[i][j], end=" ")
    print()