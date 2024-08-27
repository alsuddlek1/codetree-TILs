N = int(input())
data = [0 for i in range(N)]
for i in range(N):
    data[i] = int(input())

result = 0

for i in range(N):
    if i == 0 or data[i] != data[i-1]:
        result += 1

print(result)