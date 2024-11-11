## N*N -> 3*3 격자에서 동전 개수 최대 프로그램

# 1. 변수선언
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 2. 3*3 격자 내 동전 개수
for i in range(N-2):
    for j in range(N-2):
        cnt = 0
        for x in range(i, i+3):
            for y in range(j, j+3):
                if data[x][y] == 1:
                    cnt += 1
        result = max(result, cnt)

print(result)