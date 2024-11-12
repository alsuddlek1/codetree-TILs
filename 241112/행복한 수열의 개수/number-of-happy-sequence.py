## n*n
## 행복한 수열 : 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열

# 1. 변수 선언
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 2. 수열 찾기
# 2-1. 행 수열
for i in range(n):
    cnt = 1
    for j in range(n-1):
        if data[i][j] == data[i][j+1]:
            cnt += 1
            if cnt == m:
                answer += 1


# 2-2. 열 수열
for i in range(n):
    cnt = 1
    for j in range(n-1):
        if data[j][i] == data[j+1][i]:
            cnt += 1
            if cnt == m:
                answer += 1
print(answer)