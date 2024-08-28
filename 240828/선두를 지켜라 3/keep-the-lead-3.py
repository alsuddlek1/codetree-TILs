MAX_T = 1000000
N, M = map(int, input().split())
arr_A, arr_B = [0] * (MAX_T+1), [0] * (MAX_T+1)
time_A, time_B = 1, 1

# A
for i in range(N):
    # v : 속도, t : 시간
    v, t = map(int, input().split())
    for j in range(t):
        arr_A[time_A] = arr_A[time_A-1] + v
        time_A += 1

# B
for i in range(M):
    # v : 속도, t : 시간
    v, t = map(int, input().split())
    for j in range(t):
        arr_B[time_B] = arr_B[time_B-1] + v
        time_B += 1

# 비교
first = [0] * (MAX_T+1)
result = 0

for i in range(1, MAX_T+1):
    if arr_A[i] > arr_B[i]:
        first[i] = 1
    elif arr_A[i] < arr_B[i]:
        first[i] = 2
    elif arr_A[i] == arr_B[i]:
        first[i] = 3

for i in range(1, MAX_T+1):
    if first[i] != first[i-1]:
        result += 1

print(result-1)