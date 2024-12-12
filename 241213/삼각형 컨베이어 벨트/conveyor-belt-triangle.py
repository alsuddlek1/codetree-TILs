n, t = map(int, input().split())

data = []
for _ in range(3):
    arr = list(map(int, input().split()))
    for x in range(n):
        data.append(arr[x])

for time in range(t):
    temp = data[-1]

    for i in range(n*3-1, 0, -1):
        data[i] = data[i-1]

    data[0] = temp

for i in range(n*3):
    print(data[i], end=" ")
    if i%3 == 2:
        print()
        
