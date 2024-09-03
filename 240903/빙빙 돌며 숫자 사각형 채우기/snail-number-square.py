N, M = map(int, input().split())

snail = [[0]*N for _ in range(N)]

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

x, y = 0,0 # 달팽이 시작 위치
cnt = 1
snail[x][y] = cnt
dir = 0

while cnt < N*M:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if in_range(nx, ny) and snail[nx][ny] == 0:
        cnt += 1
        snail[nx][ny] = cnt
        x,y = nx, ny
    else:
        dir += 1
        if dir >= 4:
            dir = 0

for i in range(N):
    for j in range(M):
        print(snail[i][j], end=" ")
    print()