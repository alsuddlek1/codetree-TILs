# 1. 특정 직사각형 만들기
def square(r1, c1, r2, c2):
    square_grid = []

    for i in range(r1, r2+1):
        grid_arr = []
        for j in range(c1, c2+1):
            grid_arr.append(data[i][j])
        square_grid.append(grid_arr)

    return square_grid

# 2. 특정 직사각형 경계가 시계방향으로 shift
def shift(grid):
    n = len(grid)
    m = len(grid[0])

    # 2-1. 맨 윗줄 shift
    temp1 = grid[0][-1]
    for i in range(m-1, 0, -1):
        grid[0][i] = grid[0][i-1]
    
    # 2-2. 우측 세로 shift
    temp2 = grid[-1][-1]
    for i in range(n-1, 0, -1):
        grid[i][-1] = grid[i-1][-1]
    grid[1][-1] = temp1

    # 2-3. 맨 아래줄 shift
    temp3 = grid[-1][0]
    for i in range(1, m-1):
        grid[-1][i-1] = grid[-1][i]
    grid[-1][-2] = temp2

    # 2-4. 좌측 세로 shift
    for i in range(n-1):
        grid[i][0] = grid[i+1][0]
    grid[-2][0] = temp3

    return grid
    

# 3-1. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 3. 특정 직사각형 내 모든 숫자 십자모양의 평균값으로 값 교환
def avg_sum(x, y):
    dx = [0, 0, 1, -1] # 동서남북
    dy = [-1, 1, 0, 0]
    cnt = 1
    sum_cnt = data[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny):
            sum_cnt += data[nx][ny]
            cnt += 1
    
    avg_cnt = sum_cnt // cnt

    return avg_cnt

n, m, q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
new_data = [[0] * m for _ in range(n)]

for Q in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    grid = square(r1, c1, r2, c2)

    shift(grid)

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            data[i][j] = grid[i-r1][j-c1]

    ## --- data = 회전 후 데이터

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            new_data[i][j] = avg_sum(i, j)

    for i in range(n):
        for j in range(m):
            if new_data[i][j] == 0:
                new_data[i][j] = data[i][j]
    data = new_data
    new_data = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print()
    