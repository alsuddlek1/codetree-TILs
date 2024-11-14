# 1. 변수 설정
n, t = map(int, input().split())
data = []

for i in range(3):
    arr = list(map(int, input().split()))
    for j in range(n):
        data.append(arr[j])

# print(data)

# 2. arr 이동
for t in range(t):
    temp = data[-1]

    for i in range(3*n-2, -1, -1):
        data[i+1] = data[i]

    data[0] = temp

# 3. answer
for i in range(3*n):
    print(data[i], end=" ")
    if (i+1) % n == 0:
        print()