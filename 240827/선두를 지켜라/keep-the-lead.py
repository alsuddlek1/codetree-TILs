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
result = 0

# 이전 부호
previous_sign = (arr_A[0] - arr_B[0]) >= 0
for i in range(MAX_T):
    # 현재 부호
    current_sign = (arr_A[i] - arr_B[i]) >= 0
    if current_sign != previous_sign and current_sign != 0:
            result += 1
    previous_sign = current_sign

print(result)