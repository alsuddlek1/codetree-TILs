# 2. 가로 행복한 수열 함수
## 스택
def row_simulate(row):
    stack = []
    cnt = 0
    for i in range(n):
        if len(stack) != 0:
            if stack[-1] == row[i]:
                cnt += 1
                # print("cnt", cnt)
                if cnt == m-1:
                    for j in range(m):
                        return True
                else:
                    stack.append(row[i])
            else:
                stack = []
                stack.append(row[i])
                cnt = 0
        else:
            stack.append(row[i])
    # print(row, stack, cnt)


# 1. 변수선언
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 4. 함수 시작 위치
if m != 1:
    for i in range(n):
        if row_simulate(data[i]):
            answer += 1
            # print("answer", answer)
    for i in range(n):
        col = []
        for j in range(n):
            col.append(data[j][i])
        if row_simulate(col):
            answer += 1
            # print("answer", answer)
elif m == 1:
    answer = n+n

print(answer)
