N, M = map(int, input().split())

data = list([0]*M for _ in range(N))
cnt = 1
x,y = 0,0
data[x][y] = cnt
dir_num = 0
dx, dy = [1,0,-1,0], [0,1,0,-1] #하,우,상,좌

def in_range(x,y):
    return 0<=x<N and 0<=y<M

for i in range(2, N * M + 1):
    nx, ny = x+dx[dir_num], y+dy[dir_num]
    if not in_range(nx, ny) or data[nx][ny] != 0:
        dir_num = (dir_num+1)%4

    x,y = x+dx[dir_num], y+dy[dir_num]
    data[x][y] = i

for i in range(N):
    for j in range(M):
        print(data[i][j], end=" ")
    print()