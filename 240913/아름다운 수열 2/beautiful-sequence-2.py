n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

result = 0

for i in range(n-m+1):
    com_list = []
    for j in range(i, i+m):
        com_list.append(A[j])
    # print(com_list)
    com_list.sort()
    if com_list == B:
        result += 1

print(result)