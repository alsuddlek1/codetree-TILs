# 2. 십자모양 폭발
def expolution(r, c, data):
    dx = [0, 0, 0, -1, 1]
    dy = [-1, 0, 1, 0, 0]

    temp_data = list([-1]*n for _ in range(n))

    target = data[r][c] - 1

    if target == 0:
        data[r][c] = -1
    else:
        for t in range(1, target+1):
            for d in range(5):
                x = r + dx[d]*t
                y = c + dy[d]*t
                if 0 <= x < n and 0 <= y < n and temp_data[x][y] == -1:
                    data[x][y] = 0
    return data

# 3. 중력
def gravitation(data):
    answer_data = list([0]*n for _ in range(n))

    for i in range(n-1, -1, -1):
        for j in range(n):
            if data[i][j] != 0:
                answer_data[i][j] = data[i][j]
            else:
                for k in range(i, -1, -1):
                    if data[k][j] != 0:
                        answer_data[i][j] = data[k][j]
                        data[k][j] = 0
                        break
    
    return answer_data

# 1. 변수선언
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

## 십자열 폭발
temp_data = expolution(r, c, data)

## 중력
answer = gravitation(data)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()