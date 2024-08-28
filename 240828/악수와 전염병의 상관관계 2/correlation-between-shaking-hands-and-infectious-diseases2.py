N, K, P, T = map(int, input().split())
data = [[0]*3 for _ in range(T)]

# 감염 경험 체크 리스트
result = [0] * (N+1)
result[P] = 1

# 감염 가능 횟수 리스트
cnt = [0] * (N+1)
cnt[P] = K

# data 만들기
for i in range(T):
    t, x, y = map(int, input().split())
    data[i][0] = t
    data[i][1] = x
    data[i][2] = y

# data 정렬
data.sort(key = lambda x : (x[0], x[1]))

# ----------------

for i in range(T):
    # x가 점염 가능성 有
    if cnt[data[i][1]] >= 1:
        # y 도 감염
        if cnt[data[i][2]] >= 1:
            cnt[data[i][2]] -= 1
        # y는 첫 감염
        else:
            result[data[i][2]] = 1
            cnt[data[i][2]] = K
        cnt[data[i][1]] -= 1

    
    # y가 점염 가능성
    elif cnt[data[i][2]] >= 1:
        # x 도 감염
        if cnt[data[i][1]] >= 1:
            cnt[data[i][1]] -= 1
        # x는 첫 감염
        else:
            result[data[i][1]] = 1
            cnt[data[i][1]] = K
        cnt[data[i][2]] -= 1


result = ''.join(map(str, result[1:]))
print(result)