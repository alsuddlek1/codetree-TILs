data = input()
stack = []

for i in data:
    if len(stack) == 0:
        stack.append(i)
    else:
        top = stack[-1]
        if i != top:
            stack.pop()
        else:
            stack.append(i)

if len(stack) == 0:
    print("Yes")
else:
    print("No")