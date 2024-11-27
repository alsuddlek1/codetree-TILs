import sys

## 1. 변수선언
DIR_NUM = 4
n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 1-1. 미로 탈출 불가능 여부 판단을 위해 방문 기록 배열
## 왜 3차원이지? 2차원 배열 -> -1 로 해도 될것같은데
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n+1)
    ]
    for _ in range(n+1)
]

# 1-2. answer
elapsed_time = 0


# 2. 미로 이동
## 2-1. 우측 방향부터 시작
curr_dir = 0

## 2-2. 범위
def in_range(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

## 2-3. 해당 위치에 벽이 있으면 이동 불가
def wall_exist(x, y):
    if in_range(x,y) and a[x][y] == "#":
        return True

def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time

    # 현재 위치에서 같은 방향으로 진행한 적이 있는지 판단
    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0) # 프로그램 종료
    
    # 현재 위치 방문
    visited[curr_x][curr_y][curr_dir] = True

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌,상
    
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    # Step 1

    # 바라보고  있는 방향으로 이동하는 것이 불가능 한 경우에는
    # 반 시계 방향으로 90도 회전
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir - 1 + 4) % 4
    
    # Step 2
    ## case 1
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1
    
    # case2, 3
    else:
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]

        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1

        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2

for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(curr_x, curr_y):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(elapsed_time)