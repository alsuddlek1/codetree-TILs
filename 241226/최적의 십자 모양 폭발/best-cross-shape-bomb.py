# 2-1. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 2. 폭발
def bomb(x, y):
    size = data[x][y] - 1
    data[x][y] = -1

    dxs = [-1, 1, 0, 0] # 상,하,좌,우
    dys = [0, 0, -1, 1]
    for i in range(1, size+1):
        for dx, dy in zip(dxs, dys):
            nx = x + dx*i
            ny = y + dy*i
            if in_range(nx, ny):
                data[nx][ny] = -1
    # print(data)


# 3. 중력
def gravity():
    for i in range(n):
        arr = []
        for j in range(n):
            if data[j][i] != -1:
                arr.append(data[j][i])

        new_arr = [0 for _ in range(n)]
        for k in range(n-len(arr), n):
            new_arr[k] = arr[k-(n-len(arr))]
        for l in range(n):
            data[l][i] = new_arr[l]


# 4. 같은 수 쌍 찾기
def get_num():
    num = 0
    for i in range(n):
        for j in range(n-1):
            ## 가로
            if data[i][j] == data[i][j+1] and data[i][j] != 0:
                # if in_range(i, j+2) and data[i][j+2] != data[j][i]:
                    num += 1
            ## 세로
            if data[j][i] == data[j+1][i] and data[j][i] != 0:
                # if in_range(j+2, i) and data[j+2][i] != data[j][i]:
                    num += 1
    return num

# 1. 변수 선언
n = int(input())
first_data = [list(map(int, input().split())) for _ in range(n)]

def get_data():
    data = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            data[x][y] = first_data[x][y]
    return data

answer = 0

for i in range(n):
    for j in range(n):
        data = get_data()
        bomb(i, j)
        # bomb(2,1)
        gravity()
        get_num()
        answer = max(answer, get_num())

print(answer)

