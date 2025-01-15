k, n = map(int, input().split())

answer = []

def three_judge():
    if n < 3:
        for i in answer:
            print(i, end=" ")
        print()
        return

    has_three_consecutive = False

    for i in range(n-2):
        if answer[i] == answer[i+1] == answer[i+2]:
            has_three_consecutive = True
            break

    if not has_three_consecutive :
        for i in answer:
            print(i, end=" ")
        print()


def choose(curr_num):
    if curr_num == n+1:
        three_judge()
        return

    for i in range(1, k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()
    
    return

choose(1)