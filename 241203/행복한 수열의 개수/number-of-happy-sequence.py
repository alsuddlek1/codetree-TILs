# 2. 행복한 수열 함수
def happy(row):
    cnt = 0
    for i in range(1, n):
        if row[i-1] == row[i]:
            cnt += 1
            if cnt == m-1:
                return True
        else:
            cnt = 0 


# 1. 변수선언
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 4. 함수 시작 위치
if m != 1:
    # 행 비교
    for i in range(n):
        if happy(data[i]):
            answer += 1

    # 열 비교
    for i in range(n):
        col = []
        for j in range(n):
            col.append(data[j][i])
        if happy(col):
            answer += 1
elif m == 1:
    answer = n+n

print(answer)
