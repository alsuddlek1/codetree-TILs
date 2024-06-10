N = int(input())

data = [0] * 101

for i in range(N):
    a,b = map(int, input().split())

    for j in range(a, b+1):
        data[j] += 1

print(max(data))