# 1. 변수 선언
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 2. 범위 설정
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 3. 합 구하기
def get_num(x, y, k, l):
    cnt = 0

    # 3-1. 1/2/3/4 이동 방향
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    move_nums = [k, l, k, l] # 1/2/3/4 이동 거리

    # 3-2. move_num 이동 거리 만큼 x,y 이동하며 값 저장
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x = x + dx
            y = y + dy

            if not in_range(x, y):
                return 0
            
            cnt += grid[x][y]

    return cnt


# 4. 기울어진 직사각형 만들기
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_num(i, j, k, l))

print(ans)

