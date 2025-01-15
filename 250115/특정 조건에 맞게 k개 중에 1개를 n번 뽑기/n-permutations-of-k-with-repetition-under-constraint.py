k, n = map(int, input().split())

answer = []

def three_judge():
    for i in answer:
        print(i, end=" ")
    print()


def choose(curr_num):
    if curr_num == n:
        three_judge()
        return

    for i in range(1, k+1):
        if curr_num >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        else:
            answer.append(i)
            choose(curr_num + 1)
            answer.pop()
    
    return

choose(0)