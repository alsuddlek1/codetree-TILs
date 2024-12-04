## n*n, 최대한 "많은 금" 채굴
## k^2 + (k+1)^2 < cnt * m
## 마름모 모양
## 이차원 밖 영역 채굴 가능하지만 금 X

# 1. 변수선언
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0

# 3. 마름모 넓이
def get_area(k):
    return k * k + (k + 1) * (k + 1)

# 4. 채굴 가능한 금의 개수
def get_num_of_gold(row, col, k):
    return sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])


# 2. 마름모 만들기
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)

            # 2-1. 손해보지 않으면서 채굴할 수 있는 최대 금의 개수 저장
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)