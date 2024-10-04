## 버블 정렬 Python

N = int(input())
data = list(map(int, input().split()))

def bubble_sort(N, arr):
    sorted = True

    while sorted == False:
        for i in range(N):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = a[i+1]
                arr[i+1] = tmp
    return arr

print(bubble_sort(N, data))