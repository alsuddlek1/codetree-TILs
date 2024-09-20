N, B = map(int, input().split())

students = 0

## 한정된 양으로 가장 많은 경우를 찾는 문제 -> 정렬
data = []
for _ in range(N):
    cnt = int(input())
    data.append(cnt)

data.sort()
data[-1] = data[-1]//2
data.sort()
# print(data)

for i in range(N):
    B -= data[i]
    students += 1
    # print(B, students)
    if B <= 0:
        break

print(students)