matrix = list(list(map(int, input().split())) for _ in range(19))

## 1. 가로 정답 판단
cnt = 1
for i in range(19):
    for j in range(18):
        if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j+1]:
            cnt += 1
            if cnt == 5:
                print(matrix[i][j])
                print(i+1, j)
        else:
            cnt = 1

## 2. 세로 정답
for i in range(18):
    for j in range(19):
        if matrix[i][j] != 0 and matrix[i][j] == matrix[i+1][j]:
            cnt += 1
            if cnt == 5:
                print(matrix[i][j])
                print(i, j+1)
        else:
            cnt = 1

## 3. 좌->우 대각선
for i in range(18):
    for j in range(18):
        if matrix[i][j] != 0 and matrix[i][j] == matrix[i+1][j+1]:
            cnt += 1
            if cnt == 5:
                print(matrix[i][j])
                print(i, j)
        else:
            cnt = 1

## 3. 우 -> 좌 대각선
for i in range(19):
    for j in range(19):
        if matrix[18-i][18-j] != 0 and matrix[18-i][18-i] == matrix[18-i-1][18-i-1]:
            cnt += 1
            if cnt == 5:
                print(matrix[18-i][18-i])
                print(18-i, 18-i)
        else:
            cnt = 1