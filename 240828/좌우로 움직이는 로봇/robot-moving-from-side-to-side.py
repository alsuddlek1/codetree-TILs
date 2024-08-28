MAX_T = 50000
N, M = map(int, input().split())
arr_A, arr_B = [0] * (MAX_T + 1), [0] * (MAX_T + 1)
time_A, time_B = 1, 1

# a robot
for i in range(N):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        arr_A[time_A] = arr_A[time_A-1] + (1 if d=="R" else -1)
        time_A += 1
    for k in range(time_A, MAX_T):
        arr_A[k] = arr_A[time_A-1]

# b robot
for i in range(M):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        arr_B[time_B] = arr_B[time_B-1] + (1 if d=="R" else -1)
        time_B += 1
    for k in range(time_B, MAX_T):
        arr_B[k] = arr_B[time_B-1]

# 배열비교
result = 0
time_max = max(time_A, time_B)
for i in range(time_max):
    if arr_A[i] == arr_B[i] and arr_A[i-1] != arr_B[i-1]:
        result += 1

print(result)