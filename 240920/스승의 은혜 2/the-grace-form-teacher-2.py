N, B = map(int, input().split())

students = 0

## 한정된 양으로 가장 많은 경우를 찾는 문제 -> 정렬
data = []
for _ in range(N):
    data.append(int(input()))

data.sort()

for i in range(N):
    B -= data[i]
    students += 1
    if B <= 0:
        break

print(students)