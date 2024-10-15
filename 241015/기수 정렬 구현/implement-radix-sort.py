n = int(input())
data = list(map(int, input().split()))

data.sort()

for _ in range(n):
    print(data[_], end=" ")