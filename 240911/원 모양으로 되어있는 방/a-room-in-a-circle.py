N = int(input())
arr = []
for _ in range(N):
    c = int(input())
    arr.append(c)

res = 100000000
for i in range(N):
    # 방 바꾸기
    cnt = 0
    for j in range(N):
        # 인원수
        cnt += arr[j] * j
    res = min(cnt, res)
    arr.append(arr[0])
    arr.pop(0)
print(res)