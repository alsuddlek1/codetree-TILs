## 직사각형 만들기
# 해당 직사각형에 음수 있을 경우 false

# 1. 변수선언
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 0. 범위
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

# 2. 사각형 만들기
def judge_plus(x, y, k, l):
    cnt = 0
    for i in range(x, x+k):
        for j in range(y, y+l):
            if in_range(i, j):
                if grid[i][j] > 0:
                    cnt += 1
                else:
                    cnt = 0
                    return cnt
    return cnt

# 3. 사각형 시작점
for i in range(n):
    for j in range(m):
        # 3-1. 사각형 크기
        for k in range(1, n+1): # 세로
            for l in range(1, m+1): # 가로
                ans = max(ans, judge_plus(i, j, k, l))

print(ans)