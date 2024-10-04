## 버블 정렬 Python

N = int(input())
data = list(map(int, input().split()))

def bubble_sort(N, arr):
    for k in range(N):
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr

for i in range(N):
    print(bubble_sort(N, data)[i], end=" ")