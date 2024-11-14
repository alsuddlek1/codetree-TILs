## 2*n : 배열의 길이

## 1. 변수 선언
n, t = map(int, input().split())
data = []
for i in range(2):
    arr = list(map(int, input().split()))
    for j in range(n):
        data.append(arr[j])

# 2. 1차원 배열 밀기
# 2-1. 오른쪽으로 밀기
temp = data[-1]

for i in range(2*n-2, -1, -1):
    data[i+1] = data[i]

# 3. answer
for i in range(2*n):
    print(data[i], end=" ")
    if i == n-1:
        print()

