N, M = map(int, input().split())
matrix = list([0]*(N+1) for _ in range(N+1))

## 판단 함수
def judge(x, y):
    global matrix
    dx = [0, 0, -1, 1] # 좌우상하
    dy = [-1, 1, 0, 0]
    cnt = 0
    for dir in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<=nx<N+1 and 0<=ny<N+1 and matrix[nx][ny] == 1:
        # if matrix[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False


for i in range(M):
    x, y = map(int, input().split())

    # 색칠하기
    matrix[x][y] = 1
    done = judge(x,y)
    if done:
        print(1)
    else:
        print(0)