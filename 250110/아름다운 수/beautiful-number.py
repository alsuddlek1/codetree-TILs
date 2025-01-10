n = int(input())
answer = []
result = 0

# 2. 순열이 아름다운 수 인지 판단
def judge_num():
    
    idx = 0
    while idx < n:
        ## 연속하는 수 만큼 인덱스 이동 해야 하는데 현재 리스트보다 더 큰 인덱스가 나오면 안됨
        if idx + answer[idx] - 1 >= n:
            return False
        
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인
        for j in range(idx, idx + answer[idx]):
            if answer[j] != answer[idx]:  # 연속
                return False
            
        idx += answer[idx]     # idx는 idx번째 수 만큼 점프
        # idx가 0이고 answer[0]가 2면 2칸씩 연속한지 확인할 것임 

    return True

# 1. n자리 순열 만들기
def choosen(curr_cnt):
    global result

    if curr_cnt == n+1:
        if judge_num():
            result+=1
            
        return

    for i in range(1, 5):
        answer.append(i)
        choosen(curr_cnt+1)
        answer.pop()

    return

choosen(1)

print(result)
