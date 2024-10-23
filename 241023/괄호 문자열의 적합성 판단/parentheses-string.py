data = input()

res = "()"

def stack_solution(data):
    stack = []
    for i in range(len(data)):
        if data[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return "No"
            else:
                stack.pop()
    
    if len(stack) == 0:
        return "Yes"
    return "No"

print(stack_solution(data))