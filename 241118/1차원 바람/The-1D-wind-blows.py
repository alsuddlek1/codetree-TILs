## n*m 행렬
## 특정 행의 모든 원소들을 왼쪽 혹은 오른쪽으로 민다
## 위 아래 하나라도 같은 열에 같은 숫자가 적혀있으면 전파가 나아간다

# 2. 행을 미는 함수
def shift(arr, d):
    n = len(arr)
    if d == "L":
        temp = arr[-1]
        for i in range(n-2, -1, -1):
            arr[i+1] = arr[i]
        arr[0] = temp
    
    else:
        temp = arr[0]
        for i in range(1, n):
            arr[i-1] = arr[i]
        arr[-1] = temp
    return arr

# 4. 전파
# def spread(s, e, r, d): # s: 시작범위, e: 마지막 범위, r: r 이하 열 일때 -1/ 이상일때 1, d: R/L 방향
#     if d == "L":
#             d = "R"
#     else:
#         d = "L"

#     if r == -1:
#         j = j+1
#     else:
#         j = j-1

#     for k in range(m):
#         if data[j+1][k] == data[j][k]:
#             data[j] = shift(data[j], d)
#             break


# 1. 변수선언
n, m, q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 3. data
for i in range(q):
    r, d = input().split()
    r = int(r) - 1

    data[r] = shift(data[r], d)

    # 3-1. 0~r-1
    for j in range(r-1, -1, -1):
        d_2 = d
        if d_2 == "L":
            d_2 = "R"
        else:
            d_2 = "L"

        for k in range(m):
            if data[j+1][k] == data[j][k]:
                data[j] = shift(data[j], d_2)
                break

    # 3-1. 0~r-1
    for j in range(r+1, n, 1):
        d_2 = d
        if d_2 == "L":
            d_2 = "R"
        else:
            d_2 = "L"

        for k in range(m):
            if data[j-1][k] == data[j][k]:
                data[j] = shift(data[j], d_2)
                break

# 5. answer
for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print()