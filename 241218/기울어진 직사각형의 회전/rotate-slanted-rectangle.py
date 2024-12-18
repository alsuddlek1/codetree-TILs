# 2. 회전
def location_0(x, y, m_arr, dirs):
    # 2-1. x,y 좌표에서 1,2,3,4 방향으로 이동
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]

    square_x = []
    square_y = []

    nx, ny = x, y
    cnt = 0
    for dx, dy in zip(dxs, dys):
        for m in range(m_arr[cnt]):
            nx = nx + dx
            ny = ny + dy
            square_x.append(nx)
            square_y.append(ny)
        cnt += 1

    if dirs == 0:
        temp = data[square_x[-1]][square_y[-1]]
        for i in range(len(square_x)-1, 0, -1):
            data[square_x[i]][square_y[i]] = data[square_x[i-1]][square_y[i-1]]
        data[square_x[0]][square_y[0]] = temp
    else:
        temp = data[square_x[0]][square_y[0]]
        for i in range(len(square_x)-1):
            data[square_x[i]][square_y[i]] = data[square_x[i+1]][square_y[i+1]]
        data[square_x[-1]][square_y[-1]] = temp

    return data

# 1. 변수 선언
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
r, c , m1, m2, m3, m4, dirs = map(int, input().split())
r, c = r-1, c-1
m_list = [m1, m2, m3, m4]

answer = location_0(r, c, m_list, dirs)

# 3. 출력
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()