N = int(input())
data = list(map(int, input().split()))
data.sort()

max_value = 0
for i in range(N):
    if data[i] + data[2*N-1-i] > max_value:
        max_value = data[i] + data[2*N-1-i]

print(max_value)