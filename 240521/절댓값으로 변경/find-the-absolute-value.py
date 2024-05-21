N = int(input())
data = list(map(int, input().split()))

def absolute(N, data):
    for i in range(N):
        data[i] = abs(data[i])
    return data

for i in absolute(N, data):
    print(i, end=" ")