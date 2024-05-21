N = int(input())
data = list(map(int, input().split()))

def even(N, data):
    for i in range(N):
        if data[i] % 2 == 0:
            data[i] = data[i]//2
    return data

for i in even(N, data):
    print(i, end=" ")