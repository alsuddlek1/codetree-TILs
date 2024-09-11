N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(N):
    # cnt 
    for j in range(i+2, N):
        cnt = arr[i] + arr[j]
        result = max(cnt, result)
print(result)