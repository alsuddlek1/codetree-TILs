N, M = map(int, input().split())

snail = [[0]*M for _ in range(N)]

dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

x, y = 0, 0  # 달팽이 시작 위치
cnt = 1
snail[x][y] = cnt
dir = 0

# while cnt < N*M:
#     nx = x + dx[dir]
#     ny = y + dy[dir]
#     if in_range(nx, ny) and snail[nx][ny] == 0:
#         cnt += 1
#         snail[nx][ny] = cnt
#         x, y = nx, ny
#     else:
#         dir += 1
#         if dir >= 4:
#             dir = 0

for i in range(2, N * M + 1):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dx[dir], y + dy[dir]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전합니다.
    if not in_range(nx, ny) or snail[nx][ny] != 0:
        dir = (dir + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dx[dir], y + dy[dir]
    snail[x][y] = i

for i in range(N):
    for j in range(M):
        print(snail[i][j], end=" ")
    print()