n = int(input())
data = list(map(int, input().split()))

def insert_sort(arr):
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

insert_sort(data)
for _ in range(n):
    print(data[_], end=" ")