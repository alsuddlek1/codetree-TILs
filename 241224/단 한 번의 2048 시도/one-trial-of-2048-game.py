NONE = -1

# 1. 변수 선언
n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

# 2. grid 시계방향으로 90도 회전
## 항상 아래 방향으로 떨어뜨리기 위해
def rotate():
    # next_grid 0으로 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    # 90도 회전
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n-j-1][i]

    # next_grid를 grid에 옮기기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# 3. 중력
def drop():
    # next_grid 0으로 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    # 아래 방향으로 중력
    for j in range(n):
        # 같은 숫자끼리 단 한번만 합치기 위해 떨어뜨리기 전 숫자 하나는 keep
        keep_num, next_row = NONE, n-1

        for i in range(n-1, -1, -1):
            if not grid[i][j]:
                continue
        
        # 아직 떨어진 숫자가 없다면 갱신
            if keep_num == NONE:
                keep_num = grid[i][j]

            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num * 2
                keep_num = NONE
                
                next_row -= 1
            
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                
                next_row -= 1

        if keep_num != NONE:
            next_grid[next_row][j] = keep_num
            next_row -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def tilt(move_dir):
    for _ in range(move_dir):
        rotate()

    drop()

    for _ in range(4-move_dir):
        rotate()

dir_char = input()

dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

# 기울이기
tilt(dir_mapper[dir_char])

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()