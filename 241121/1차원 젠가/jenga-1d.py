# 2. 제거 함수
def delete(s, e, arr):
    temp_arr = []
    for i in range(s, e+1):
        arr[i] = -1
    for i in range(len(arr)):
        if arr[i] != -1:
            temp_arr.append(arr[i])

    return temp_arr

# 1. 변수설정
n = int(input())

arr = [0] * n
for _ in range(n):
    arr[_] = int(input())

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s1, e1, s2, e2 = s1-1, e1-1, s2-1, e2-1

arr = delete(s1, e1, arr)
arr = delete(s2, e2, arr)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])


