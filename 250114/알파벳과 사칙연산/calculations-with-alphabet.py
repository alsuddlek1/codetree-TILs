input_formula = input()
formula = []
calculation = ["+", "-", "*"]
num_cnt = 0
answer = -1000000

for i in input_formula:
    if i not in calculation:
        num_cnt += 1
    else:
        formula.append(i)

## 2. num 숫자와 formula 연산 조합해서 가장 큰 수 출력
# 2-1. 예) num[0] formula[1] num[1] formula[2] num[2]
def calculate():
    cnt = num[0]
    for i in range(1, num_cnt):
        if formula[i-1] == "+":
            cnt = cnt + num[i]
        elif formula[i-1] == "-":
            cnt = cnt - num[i]
        elif formula[i-1] == "*":
            cnt = cnt * num[i]

    return cnt
    

## 1. 식의 변수 수에 맞는 num_cnt 자리 수 백트래킹
num = []
def back(curr_num):
    global answer
    if curr_num == num_cnt+1:
        answer = max(answer, calculate())
        return
    
    for i in range(1, 5):
        num.append(i)
        back(curr_num + 1)
        num.pop()
    
    return

back(1)

print(answer)