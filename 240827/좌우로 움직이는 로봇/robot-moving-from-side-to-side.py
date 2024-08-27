MAX_T = 50000

def process_commands(N, commands, arr):
    time = 0
    idx = 0
    
    for i in range(N):
        t, d = commands[i]
        t = int(t)
        for j in range(t):
            if d == "R":
                arr[idx] = time
                time += 1
            else:
                arr[idx] = time
                time -= 1
            idx += 1
        for k in range(idx, MAX_T):
            arr[k] = time

def main():
    N, M = map(int, input().split())
    arr_A, arr_B = [0] * MAX_T, [0] * MAX_T
    
    commands_A = [input().split() for _ in range(N)]
    commands_B = [input().split() for _ in range(M)]
    
    process_commands(N, commands_A, arr_A)
    process_commands(M, commands_B, arr_B)
    
    # 판별
    cnt = 0
    for i in range(1, MAX_T):
        if arr_A[i] == arr_B[i] and arr_A[i-1] != arr_B[i-1]:
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()