# 3. 범위
def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

# 2. 폭발 함수
def bomb(size, x, y):
    dxs = [0, -1, 1, 0, 0] # 상, 하, 좌, 우
    dys = [0, 0, 0, -1, 1]
    if size == 1:
        grid[x][y] = 0
    else:
        for s in range(1, size):
            for dx, dy in zip(dxs, dys):
                nx = x + dx*s
                ny = y + dy*s
                if in_range(nx, ny) and grid[nx][ny] != 0:
                    grid[nx][ny] = 0
                    ## 중력

 # 4. 중력
def gravity():
    for i in range(n):
        arr = []
        for j in range(n):
            if grid[j][i] != 0:
                arr.append(grid[j][i])

        new_arr = [0 for _ in range(n)]
        for k in range(n-len(arr), n):
            new_arr[k] = arr[k-(n-len(arr))]
        for l in range(n):
            next_grid[l][i] = new_arr[l]

# 1. 변수 선언
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]
for c in range(m):
    c = int(input()) - 1
    for i in range(n):
        if grid[i][c] != 0:
            size = grid[i][c]
            bomb(size, i, c)
            gravity()
            break

for i in range(n):
    for j in range(n):
        print(next_grid[i][j], end=" ")
    print()