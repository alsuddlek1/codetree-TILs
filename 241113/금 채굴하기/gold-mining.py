## n*n에서 최대한 많은 금
## 마름모 모양

# 금 개수 * m >= K^2 + (K+1)*2

# 1. 변수선언
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 2. 마름모 넓이
def get_area(k):
    return k*k + (k+1)*(k+1)

# 3. k에 대하여 채굴 가능한 금의 개수
def get_num_of_gold(row, col, k):
    return sum([
        data[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2*(n-1)+ 1):
            num_of_gold = get_num_of_gold(row, col, k)

            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)