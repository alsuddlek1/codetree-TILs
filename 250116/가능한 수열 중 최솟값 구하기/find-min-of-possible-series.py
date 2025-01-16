import sys

n = int(input())
found = False

# 1. 모든 수열 만들기 (백트래킹)
def back(curr_num):
    global found
    if found:
        return

    # 현재 길이까지 좋은 수열인지 판단
    for length in range(1, curr_num // 2 + 1):
        if sequence[-length:] == sequence[-2 * length:-length]:
            return  # 나쁜 수열이면 가지치기

    # 길이가 n이면 출력하고 종료
    if curr_num == n + 1:
        found = True
        print("".join(map(str, sequence)))
        return

    # 수열 확장
    for i in range(4, 7):
        sequence.append(i)
        back(curr_num + 1)
        sequence.pop()

# 초기화
sequence = []
back(1)
