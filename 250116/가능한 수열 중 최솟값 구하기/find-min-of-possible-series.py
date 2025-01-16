import sys

n = int(input())
found = False

# 2. 불가능한 수열 판단
def get_possible():
    global found

    if found:
        return

    for i in range(n):
        slice_seq = sequence[i:]
        # print(i, slice_seq)
        for j in range(1, len(slice_seq)//2+1):
            check = slice_seq[:j]
            # print("check",j, check)
            # print("slice", slice_seq[j:j+j])
            if check == slice_seq[j:j+j]:
                return
    
    found = True
    for i in sequence:
        print(i, end="")
    return
    

# 1. 모든 수열 만들기
sequence = []
def back(curr_num):
    global found
    if found:
        return
    if curr_num == n+1:
        get_possible()
        return

    for i in range(4, 7):
        sequence.append(i)
        back(curr_num + 1)
        sequence.pop()

    return

back(1)