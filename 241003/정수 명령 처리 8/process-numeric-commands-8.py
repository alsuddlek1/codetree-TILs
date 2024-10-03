N = int(input())
arr = []

for _ in range(N):
    data = input().split()
    if len(data) == 2:
        data[1] = int(data[1])
        if data[0] == "push_front":
            arr.insert(0, data[1])
        elif data[0] == "push_back":
            arr.append(data[1])
    else:
        if data[0] == "pop_front":
            print(arr[0])
            arr.pop(0)
        elif data[0] == "pop_back":
            print(arr[-1])
            arr.pop()
        elif data[0] == "size":
            print(len(arr))
        elif data[0] == "empty":
            if len(arr) == 0:
                print(1)
            else:
                print(0)
        elif data[0] == "front":
            print(arr[0])
        elif data[0] == "back":
            print(arr[-1])