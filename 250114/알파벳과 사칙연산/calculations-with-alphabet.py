input_expression = input()
alphabet_list = []
calculation_list = []
answer = -1000000

calculation = ["+", "-", "*"]
for i in input_expression:
    if i not in calculation:
        alphabet_list.append(i)
    else:
        calculation_list.append(i)

alphabet_to_index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}

# 2. calculate
def calculate():
    # 2-1. 알파벳 별 index 지정
    num_index = [alphabet_to_index[char] for char in alphabet_list]
    
    # 2-1. num_list의 num_index에 맞추어 계산
    cnt = num_list[num_index[0]]
    for i in range(len(num_index)-1):
        if calculation_list[i] == "+":
            cnt += num_list[num_index[i+1]]
        elif calculation_list[i] == "-":
            cnt -= num_list[num_index[i+1]]
        elif calculation_list[i] == "*":
            cnt *= num_list[num_index[i+1]]

    return cnt

# 1. a~f 수 할당
num_list = []
def back(curr_num):
    global answer
    if curr_num == 6:
        answer = max(answer, calculate())
        return

    for i in range(1, 5):
        num_list.append(i)
        back(curr_num + 1)
        num_list.pop()
    return

back(0)
print(answer)