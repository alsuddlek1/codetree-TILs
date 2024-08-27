MAX_T = 50000
N, M = map(int, input().split())
arr_A, arr_B = [0] * MAX_T, [0] * MAX_T
time_A, time_B = 0, 0
idx_A, idx_B = 0, 0

# A 로봇
for i in range(N):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d == "R":
            arr_A[idx_A] = time_A
            time_A = time_A + 1
            idx_A += 1
        else:
            arr_A[idx_A] = time_A
            time_A = time_A - 1
            idx_A += 1
    # for k in range(idx_A, MAX_T):
    #     arr_A[k] = time_A
    length = len(arr_A[idx_A:])
    arr_A[idx_A:] = [time_A] * length

# B 로봇
for i in range(M):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d == "R":
            arr_B[idx_B] = time_B
            time_B = time_B + 1
            idx_B += 1
        else:
            arr_B[idx_B] = time_B
            time_B = time_B - 1
            idx_B += 1
    # for k in range(idx_B, MAX_T):
    #     arr_B[k] = time_B
    length = len(arr_B[idx_B:])
    arr_B[idx_B:] = [time_B] * length

# 판별
cnt = 0
for i in range(1, len(arr_A)):
    if arr_A[i] == arr_B[i] and arr_A[i-1] != arr_B[i-1]:
        cnt += 1

print(cnt)