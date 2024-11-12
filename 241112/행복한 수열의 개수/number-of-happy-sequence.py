## n*n
## 행복한 수열 : 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열

# 각 열/행 -> def 비교

# 1. 변수선언
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 2. 비교 함수
def check_happy(arr, m):
    cnt = 1
    # 2-1. 비교할 리스트가 맞으면 ture 아니면 false 반환
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            cnt += 1
            if cnt >= m:
                return True
        else:
            cnt = 1
    if m == 1:
        return True
    return False

# 3. 행 비교
for i in range(n):
    if check_happy(data[i], m):
        answer += 1
    
# 4. 열 비교
for i in range(n):
    row_arr = []
    for j in range(n):
        row_arr.append(data[j][i])
    if check_happy(row_arr, m):
        answer += 1

print(answer)