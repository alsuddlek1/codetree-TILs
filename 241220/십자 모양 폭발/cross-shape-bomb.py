# 3. 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 2. 십자폭발
def boom(data, x, y):
    power = data[x][y] - 1
    data[x][y] = 0

    dxs = [-1, 1, 0, 0] # 상하좌우
    dys = [0, 0, -1, 1]

    for p in range(1, power+1):
        for dx, dy in zip(dxs, dys):
            nx = x + dx*p
            ny = y + dy*p
            if in_range(nx, ny):
                data[nx][ny] = 0
    return data

# 4. 중력
def gravity_1(arr):
    new_arr = []
    return_arr = [0] * n

    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])

    for i in range(n-len(new_arr), n):
        return_arr[i] = new_arr[i-(n-len(new_arr))]

    return return_arr


# 1. 변수선언
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
s1, s2 = map(int, input().split())
s1, s2 = s1-1, s2-1
answer = [[0]*n for _ in range(n)]

data = boom(data, s1, s2)
# data = gravity(data)

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(data[j][i])

    new_arr = gravity_1(arr)
    for k in range(n):
        answer[k][i] = new_arr[k]
    

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()