## 2. explosion
def explosion(n, m, arr):
    temp_arr = []
    return_value = False

    len_n = len(arr)

    for i in range(len_n-m+1):
        cnt = 0
        index = []
        for j in range(i, len_n):
            if arr[i] == arr[j]:
                cnt += 1
                index.append(j)
            else:
                break
        
        if cnt >= m:
            return_value = True
            for k in range(len(index)):
                arr[index[k]] = -1
            # break

    for i in range(len_n):
        if arr[i] != -1:
            temp_arr.append(arr[i])
    return temp_arr, return_value

## 1. 변수 선언
n, m = map(int, input().split())
arr = [0] * n
for _ in range(n):
    arr[_] = int(input())

## 3. 폭발할 원소가 남을 때 까지 반복
while True:
    arr, value = explosion(n, m, arr)
    if value == False:
        break


## 4. 결과
print(len(arr))
for i in range(len(arr)):
    print(arr[i])