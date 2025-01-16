import sys

n = int(input())
found = False

# 1. 모든 수열 만들기 - 백트래킹
def back(curr_num):
    global found
    if found:
        return

    for length in range(1, curr_num // 2 + 1):
        if sequence[-length:] == sequence[-2 * length:-length]:
            return

    if curr_num == n + 1:
        found = True
        print("".join(map(str, sequence)))
        return

    for i in range(4, 7):
        sequence.append(i)
        back(curr_num + 1)
        sequence.pop()

sequence = []
back(1)
