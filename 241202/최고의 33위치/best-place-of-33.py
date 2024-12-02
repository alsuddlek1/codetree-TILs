# 2. 3*3 1개수 판독 함수
def simulate(s1, s2):
    cnt = 0
    for i in range(s1, s1+3):
        for j in range(s2, s2+3):
            if data[i][j] == 1:
                cnt += 1
    return cnt

# 1. 변수 선언
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 3. data에서 simulate 함수 실행

for i in range(n-2):
    for j in range(n-2):
        # i, j => simulate 시작 점
        count = simulate(i,j)
        if count >= answer:
            answer = count

print(answer)