n = int(input())
stack = []

for i in range(n):
    data = input().split()
    if len(data) == 2:
        stack.append(data[1])
        
    else:
        if data[0] == "pop":
            print(stack[-1])
            stack.pop()
        elif data[0] == "size":
            print(len(stack))
        elif data[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif data[0] == "top":
            print(stack[-1])