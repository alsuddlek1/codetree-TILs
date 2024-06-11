n = int(input())
data = [0] * 21
start = 10

for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == "R": # black : 1
        for i in range(start, start+a):
            data[i] = 1
        start += a
    
    elif b == "L": # white : 3
        for j in range(start-a, start):
            data[j] = 3
        start -= a

black = 0
white = 0
for i in range(len(data)):
    if data[i] == 1:
        black += 1
    elif data[i] == 3:
        white += 1

print(white, black)