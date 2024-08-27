N = int(input())
data = [0 for i in range(N)]
for i in range(N):
    data[i] = int(input())

result = 0
cnt = 0

for i in range(N):
    ## N=7
    ## i=0,1,2,3,4,5,6
    if i == 0 or data[i-1] == data[i]:
        cnt += 1
        if cnt >= result:
            result = cnt

print(result)