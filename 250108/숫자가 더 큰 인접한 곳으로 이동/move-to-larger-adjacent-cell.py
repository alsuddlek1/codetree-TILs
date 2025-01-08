n, r, c = map(int, input().split())
r,c = r-1, c-1
data = [list(map(int, input().split())) for _ in range(n)]
max_cnt = data[r][c]
answer = [data[r][c]]
x, y = r, c

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x,y, max_cnt):
    value = False

    dxs = [-1, 1, 0, 0] # 상하좌우
    dys = [0, 0, -1, 1]

    max_pos = (x, y)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and data[nx][ny] > max_cnt:
            max_cnt = data[nx][ny]
            max_pos = (nx, ny)
            value = True
            break
    x, y = max_pos

    return max_cnt, max_pos, value

while True:
    max_cnt, max_pos, value = move(x, y, max_cnt)
    
    if value == False:
        break

    x, y = max_pos[0], max_pos[1]
    answer.append(data[x][y])
    

for i in answer:
    print(i, end=" ")