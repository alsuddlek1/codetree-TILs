# 1. 변수 선언
n, m, k = map(int, input().split())
k = k-1
grid = [list(map(int, input().split())) for _ in range(n)]

# 1-1. 0번째 열부터 시작, 0번째 행부터 아래로 내려가기 
x, y = 0, k


# 2-1. 범위 설정
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 2. 맞닿는 지 확인
def check(r, k):
    for i in range(m):
        # 행은 아래로, 열은 m 길이 만큼
        if grid[r+1][k+i] == 1:
            return False
    return True

while True:
    if in_range(x, y) and check(x, y):
        x += 1
    else:
        for i in range(m):
            grid[x][y+i] = 1
        
        break

# 3. 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()