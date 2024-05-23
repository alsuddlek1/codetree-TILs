N, M = map(int, input().split())
arr = list(map(int, input().split()))

def array(N, M, arr):
    result = 0
    while M > 0:
        if M % 2 != 0:
            result += arr[M-1]
            M -= 1
        else:
            result += arr[M-1]
            M = M // 2
    return result

print(array(N, M, arr))