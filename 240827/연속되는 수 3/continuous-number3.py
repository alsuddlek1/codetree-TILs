N = int(input())
data = [0 for i in range(N)]
## 1. data만들기
for i in range(N):
    data[i] = int(input())

## 2. cnt : 연속 횟수 res : 최대 연속 횟수
cnt, res = 0, 0

## 3. i == 0 또는 data[i-1], data[i] 부호가 같으면 cnt = 1 로 초기화
for i in range(N):
    if i==0:
        cnt = 1
    elif data[i-1] < 0:
        if data[i] < 0:
            cnt += 1
        else:
            cnt = 1
    elif data[i-1] > 0:
        if data[i] > 0:
            cnt += 1
        else:
            cnt = 1

    if cnt >= res:
        res = cnt
print(res)