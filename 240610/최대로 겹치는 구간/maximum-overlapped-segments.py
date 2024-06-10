N = int(input())

data = [0] * 200

for i in range(N):
    a,b = map(int, input().split())
    a += 100
    b += 100

    for j in range(a, b):

        data[j] += 1

print(max(data))