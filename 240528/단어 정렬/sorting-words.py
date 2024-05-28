N = int(input())

result = []
for i in range(N):
    result.append(input())

result.sort()

for i in result:
    print(i)