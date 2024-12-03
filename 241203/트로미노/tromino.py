# 1. 변수 설정
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 2. 모형별 좌표
def simulate(x, y):
    patterns = [
        [(0, 0), (1, 0), (1, 1)],  # 3-1
        [(0, 0), (1, 0), (1, -1)], # 3-2
        [(0, 0), (0, 1), (1, 1)],  # 3-3
        [(0, 0), (0, 1), (1, 0)],  # 3-4
        [(0, 0), (0, 1), (0, 2)],  # 3-5
        [(0, 0), (1, 0), (2, 0)]   # 3-6
    ]

    max_sum = 0
    for pattern in patterns:
        cnt = 0
        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                cnt += data[nx][ny]
        # print(cnt)
        max_sum = max(max_sum, cnt)
    return max_sum


# 3. 함수 호출
answer = 0
for x in range(n):
    for y in range(m):
        answer = max(answer, simulate(x, y))

print(answer)