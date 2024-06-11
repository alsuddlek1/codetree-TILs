n = int(input())
data = [0] * 2001
color = [0] * 2001
stand = 1000

# 3 : black
# 5 : white
# 7 : gray

for i in range(n):
    a, b = input().split()
    a = int(a)

    if b == "R":
        for j in range(stand, stand+a):
            data[j] += 1
            if data[j] == 4:
                color[j] = 7
            else:
                color[j] = 3
        stand += a
    elif b == "L":
        for j in range(stand-a, stand):
            data[j] += 1
            if data[j] == 4:
                color[j] = 7
            else:
                color[j] = 5
        stand -= a

# print(color)
# print(data)
    
white = 0
black = 0
gray = 0

for k in range(len(data)):
    if color[k] == 5:
        white += 1
    elif color[k] == 3:
        black += 1
    elif color[k] == 7:
        gray += 1

print(white, black, gray)