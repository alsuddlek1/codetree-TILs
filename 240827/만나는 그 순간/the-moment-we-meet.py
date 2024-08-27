MAX_T = 1000000

N, M = map(int, input().split())
arr_A = [0] * (MAX_T + 1)
arr_B = [0] * (MAX_T + 1)


# A 이동방향
time_a = 1
for _ in range(N):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        arr_A[time_a] = arr_A[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(M):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        arr_B[time_b] = arr_B[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

result = -1
for i in range(1, time_a):
    if arr_A[i] == arr_B[i]:
        result = i
        break

print(result)