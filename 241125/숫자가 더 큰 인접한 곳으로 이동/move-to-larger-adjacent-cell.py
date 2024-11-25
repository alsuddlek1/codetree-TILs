# 2. 인접 이동 함수
def simulate(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    num_list = [data[x][y]]

    while True:
        curr_value = data[x][y]
        found = False

        for d in range(4):
            curr_x = x + dx[d]
            curr_y = y + dy[d]

            if 0 <= curr_x < n and 0 <= curr_y < n and data[curr_x][curr_y] > curr_value:
                x, y =curr_x, curr_y
                num_list.append(data[curr_x][curr_y])
                found = True
                break
    
        if found == False:
            break

    return num_list


# 1. 변수 선언
n, r, c = map(int, input().split())  # r, c : 시작 좌표
r, c = r - 1, c - 1  
data = [list(map(int, input().split())) for _ in range(n)]


num_list = simulate(r, c)

for ans in num_list:
    print(ans, end=" ")