N, M = map(int, input().split())
MAX_T = 1000000
arr_A, arr_B = [0] * (MAX_T+1),[0] * (MAX_T+1)
time_A = 1
time_B = 1

## A 배열
for i in range(N):
    v, t = map(int, input().split())
    for j in range(t):
        arr_A[time_A] += arr_A[time_A-1] + v
        time_A += 1

## B 배열
for i in range(M):
    v, t = map(int, input().split())
    for j in range(t):
        arr_B[time_B] += arr_B[time_B-1] + v
        time_B += 1

## 선두 비교
cnt = 0
leader = 0
for i in range(MAX_T):
    if arr_A[i] > arr_B[i]:
        if leader == 1:
            cnt += 1
        leader = 2
    elif arr_A[i] < arr_B[i]:
        if leader == 2:
            cnt += 1
        leader = 1

print(cnt)