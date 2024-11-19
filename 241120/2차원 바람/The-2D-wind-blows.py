import copy
## N*M 행렬, 총 Q번 바람

# 3. 십자가 평균 함수
def avg(data):
    dx = [0, 0, 0, -1, 1]
    dy = [-1, 0, 1, 0, 0]

    cnt = 0
    count = 0

    for d in range(len(dx)):
        if 0 <= i+dx[d] < n and 0 <= j+dy[d] < m:
            cnt += data[i+dx[d]][j+dy[d]]
            count += 1

    result = cnt // count

    return result

# 2. shift 함수
# 2-1. 상단 가로 -> 우측세로 -> 하단 가로-> 좌측 세로
def shift(r1, c1, r2, c2, data):
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    # 1. 상단 가로
    temp1 = data[r1][c2]
    
    for i in range(c2-1, c1-1, -1):
        data[r1][i+1] = data[r1][i]
    
    # 2. 우측 세로
    temp2 = data[r2][c2]
    
    for i in range(r2-1, r1, -1):
        data[i+1][c2] = data[i][c2]

    data[r1+1][c2] = temp1
    
    # 3. 하단 가로
    temp3 = data[r2][c1]

    for j in range(c1+1, c2):
        data[r2][j-1] = data[r2][j]
        
    data[r2][c2-1] = temp2

    # 4. 좌측 세로
    for i in range(r1+1, r2):
        data[i-1][c1] = data[i][c1]

    data[r2-1][c1] = temp3

    # 5. 특정 직사각형 행렬
    # for i in range(n):
    #     print(data[i])
    
    return data



# 1. 변수 선언
n, m, q = map(int, input().split())
data = [list(map(int ,input().split())) for _ in range(n)]

# answer = list([0]*m for _ in range(n))
answer = copy.deepcopy(data)

# for i in range(n):
#     for j in range(m):
#         answer[i][j] = data[i][j]


for Q in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    # 1-1. shift
    shift(r1, c1, r2, c2, data)

    # 1-2. shift 한 행렬 -> 평균값)
    for i in range(r1-1, r2):
        for j in range(c1-1, c2):
            answer[i][j] = avg(data)
    data = copy.deepcopy(answer)
    

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()