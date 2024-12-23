# 2. sequnce
def sequnce(m, arr):
    N = len(arr)
    return_arr = []
    return_value = False
    
    for i in range(N-m+1):
        index_list = [i]
        cnt = 1
        for j in range(i+1, N):
            if arr[i] == arr[j]:
                index_list.append(j)
                cnt += 1
            else:
                break
        if cnt >= m:
            return_value = True
            for k in index_list:
                arr[k] = -1

    for l in range(N):
        if arr[l] != -1:
            return_arr.append(arr[l])        

    return return_arr, return_value

# 1. 변수 선언
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

new_Arr = [0]

while True:
    arr, value = sequnce(m, arr)
    if value == False:
        break

# 3. 출력
print(len(arr))
for i in arr:
    print(i)