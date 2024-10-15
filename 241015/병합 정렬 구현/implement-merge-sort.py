n = int(input())
data = list(map(int, input().split()))

data.sort()
for i in range(n):
    print(data[i], end=" ")