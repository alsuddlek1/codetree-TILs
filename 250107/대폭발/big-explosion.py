n, m, r, c = map(int, input().split())
r, c = r-1, c-1

# Write your code here!
grid = [[0 for _ in range(n)] for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

# 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 폭발
def expand(x, y, dist):
    dxs = [-1, 1, 0, 0] # 상 하 좌 우
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx = x + dx * dist
        ny = y + dy * dist
        if in_range(nx, ny):
            next_grid[nx][ny] = 1

#
def simulate(dist):
    # next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    # 폭탄이 있을 때
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                expand(i, j, dist)
    
    # next_grid에서 폭발 한 후 -> grid에 옮기기
    for i in range(n):
        for j in range(n):
            if next_grid[i][j]:
                grid[i][j] = 1

grid[r][c] = 1
dist = 1
for M in range(m):
    simulate(dist)
    dist *= 2

result = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            result += 1

print(result)