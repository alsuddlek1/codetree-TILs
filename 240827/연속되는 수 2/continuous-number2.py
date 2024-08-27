N = int(input())
data = [0 for i in range(N)]
for i in range(N):
    data[i] = int(input())

result = 0
cnt = 0

for i in range(N):
    if i == 0 or data[i-1] == data[i]:
        cnt += 1
    else:
        cnt = 1
    # print(i, cnt)
    if cnt >= result:
        result = cnt
        
print(result)