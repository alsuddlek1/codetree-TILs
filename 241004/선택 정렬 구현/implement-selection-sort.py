N = int(input())
data = list(map(int, input().split()))

def selection_sort(N, arr):
    for i in range(N-1):
        minimum = i
        for j in range(i+1, N):
            if arr[j] < arr[minimum]:
                minimum = j
        tmp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = tmp
    return arr

selection_sort(N, data)
for i in range(N):
    print(data[i], end=" ")