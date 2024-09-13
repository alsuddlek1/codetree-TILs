N = int(input())
data = list(map(int, input().split()))

result = 0
avg_list = []

for i in range(N):
    for j in range(i, N):
        for k in range(i, j+1):
            avg_list.append(data[k])
        mean = sum(avg_list)/len(avg_list)
        if mean in avg_list:
            result += 1
        avg_list = []

print(result)