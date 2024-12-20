# 3. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 2. 십자폭발
def boom(data, x, y):
    power = data[x][y] - 1
    data[x][y] = 0

    dxs = [-1, 1, 0, 0] # 상하좌우
    dys = [0, 0, -1, 1]

    for p in range(1, power+1):
        for dx, dy in zip(dxs, dys):
            nx = x + dx*p
            ny = y + dy*p
            if in_range(nx, ny):
                data[nx][ny] = 0
    return data

# 4. 중력
def gravity(data):
    # 아래에서부터 data[i][j] == 0 이면 data[i][j] = data[i-1][j]
    for i in range(n-1, 0, -1):
        for j in range(n):
            if data[i][j] == 0:
                data[i][j] = data[i-1][j]
                data[i-1][j] = 0
    return data


# 1. 변수선언
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
s1, s2 = map(int, input().split())
s1, s2 = s1-1, s2-1

data = boom(data, s1, s2)
data = gravity(data)

for i in range(n):
    for j in range(n):
        print(data[i][j], end=" ")
    print()