n, m, k = map(int, input().split())
n_distance = list(map(int, input().split()))
answer = 0

# 2. 백트래킹 리스트 -> 최대 얻을 수 있는 크기 구하기
def get_score():
    score = 0
    score_list = [0 for _ in range(k)]
    # 2-1. distances -> n_distance 조합
    for i in range(n):
        score_list[distances[i]-1] += n_distance[i]

    # 2-2. score_list[i] >= m: answer += 1
    for i in score_list:
        if i >= m-1:
            score += 1

    return score


# 1. n만큼의 길이로 백트래킹 list
distances = []
def choose(curr_num):
    global answer
    if curr_num == n+1:
        answer = max(get_score(), answer)
        return

    for i in range(1, k+1):
        distances.append(i)
        choose(curr_num + 1)
        distances.pop()
    
    return

choose(1)

print(answer)