N = int(input())
stand = 100
data = [0] * 201

for i in range(N):
    a, b = input().split()
    a = int(a)
    
    if b == "R":
        for j in range(stand, stand+a):
            data[j] += 1
        stand += a
    
    if b == "L":
        for j in range(stand-a, stand):
            data[j] += 1
        stand -= a
    
result = 0
for k in range(201):
    if data[k] > 1:
        result += 1

print(result)