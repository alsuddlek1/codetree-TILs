# 특정 행을 왼/오 shift
# shift 된 위 아래 행은 반대로 shift

# 2. 특정 행 shift
def shift(arr, w):
    if w == "L":
        temp = arr[-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp

        temp = arr[0]
        return arr
    else:
        temp = arr[0]
        for i in range(1, len(arr)):
            arr[i-1] = arr[i]
        arr[-1] = temp
        return arr


# 3. 같은 수 판단
def same_num_judge(arr1, arr2):
    for i in range(m):
        if arr1[i] == arr2[i]:
            return True

# 5. 방향 뒤짚기
def wind(w):
    if w == "L":
        w = "R"
    else:
        w = "L"
    return w


# 1. 변수 선언
n, m, q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
r, d = input().split()
r = int(r) - 1

# 4. 전파
for Q in range(q):
    shift(data[r], d)
    d_2 = wind(d)

    # 4-1. 0 ~ r-1
    for i in range(r-1, -1, -1):
        if same_num_judge(data[i+1], data[i]):
            shift(data[i], d_2)
            d_2 = wind(d_2)
        else:
            break

    d_2 = d
    d_2 = wind(d)

    # 4-2. r+1 ~ n
    for i in range(r+1, n):
        if same_num_judge(data[i-1], data[i]):
            shift(data[i], d_2)
            d_2 = wind(d_2)
        else:
            break

for i in range(n):
    for j in range(m):
        print(data[i][j], end=" ")
    print()