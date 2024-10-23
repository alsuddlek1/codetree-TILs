n = int(input())
queue = []

for i in range(n):
    data = input().split()
    if len(data) == 2:
        queue.append(int(data[1]))
    else:
        if data[0] == "pop":
            print(queue[0])
            queue.pop(0)
        elif data[0] == "size":
            print(len(queue))
        elif data[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        else:
            print(queue[0])