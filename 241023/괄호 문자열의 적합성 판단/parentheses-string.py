data = input()
stack = []
result = "()"
res = ""

for i in data:
    if i == "(" and len(stack) == 0:
        stack.append(i)
    else:
        if len(stack) > 0:
            top = stack[-1]
            if i != top:
                stack.pop()
            else:
                stack.append(i)
   

if len(stack) == 0:
    print("Yes")
else:
    print("No")