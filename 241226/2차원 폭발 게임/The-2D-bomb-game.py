# 4. 회전
def rotate():
    ## 시계방향 90도
    next_grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n):
            next_grid[j][i] = data[n-i-1][j]
    return next_grid



# 3. 중력
def gravity():
    for i in range(n):
        arr = []
        for j in range(n):
            if data[j][i] != 0:
                arr.append(data[j][i])
        next_arr = [0 for _ in range(n)]
        for k in range(n-len(arr),n):
            next_arr[k] = arr[k - (n-len(arr))]
        for l in range(n):
            data[l][i] = next_arr[l]
            

# 2. m개 이상 폭발
def bomb(m):
    value = False
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(data[j][i])

        for k in range(n-m+1):
            bomb_index = []
            for l in range(k, n):
                if arr[k] == arr[l] and arr[k] != 0:
                    bomb_index.append(l)
                else:
                    break
            
            if len(bomb_index) >= m:
                value = True
                for p in bomb_index:
                    arr[p] = 0
                
        for x in range(n):
            data[x][i] = arr[x]

    return value




# 1. 변수선언
n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 5. k번 반복
for i in range(k):
    ## bomb과 gravity -> 더이상 터질 게 없을 때 까지 반복
    while True:
        value = bomb(m)
        gravity()
        
        if value == False:
            break

    # 더이상 터질게없다면 회전
    data = rotate()
    gravity()

    while True:
        value = bomb(m)
        gravity()
        
        if value == False:
            break

    

# 6. 출력
answer = 0
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            answer += 1

print(answer)