n = int(input())
data = list(map(int, input().split()))

result = []
for i in range(n):
    if data[i] % 2 != 0:
        result.append(data[:i+1][(i+1)//2])
print(*result)