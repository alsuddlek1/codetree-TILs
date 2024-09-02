N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1,0,-1,0]

result = 0
for k in range(N):
    for l in range(N):
        # data[k][l] 의 상하좌우 판단
        cnt = 0
        for i in range(4):
            nx, ny = k + dx[i], l + dy[i]
            if in_range(nx, ny) and data[nx][ny] == 1:
                cnt += 1
                # print(nx,ny,cnt)
                if cnt >= 3:
                    result += 1
                    # print(k,l,result)
                    break
print(result)