# 1. 변수 선언
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0

# 2. 비용 == 마름모 크기
def get_area(k):
    area = k*k + (k+1)*(k+1)
    return area

# 3. 마름모 범위 내 금 개수 구하기
def get_num_of_gold(x, y, k):
    cnt_gold = 0
    for i in range(n):
        for j in range(n):
            distance = abs(x-i) + abs(y-j)
            if distance <= k:
                cnt_gold += grid[i][j]
    return cnt_gold

# 4. 중심 좌표에서 마름모 비교
for x in range(n):
    for y in range(n):
        for k in range(2*(n-1) + 1):
            num_of_gold = get_num_of_gold(x, y, k)

            # 5. 비용과 수익 비교
            if num_of_gold * m >= get_area(k):
                max_gold = max(num_of_gold, max_gold)

print(max_gold)
