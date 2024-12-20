# 1. 
def delete(s, e, arr):
    new_arr = []
    n = len(arr)

    for i in range(s, e+1):
        arr[i] = -1
    for j in range(n):
        if arr[j] != -1:
            new_arr.append(arr[j])

    return new_arr

n = int(input())
arr = [int(input()) for _ in range(n)]


for _ in range(2):
    s, e = map(int, input().split())
    s, e = s-1, e-1

    arr = delete(s, e, arr)

print(len(arr))
for i in arr:
    print(i)